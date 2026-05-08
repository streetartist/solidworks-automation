# GetDependencies Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDependencies`

Gets all of this model's dependencies.
Gets all of this model's dependencies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDependencies( _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean, _
   ByVal ListBrokenRefs As System.Boolean, _
   ByVal AppendImportedPaths As System.Boolean _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim ListBrokenRefs As System.Boolean
Dim AppendImportedPaths As System.Boolean
Dim value As System.Object
 
value = instance.GetDependencies(Traverseflag, Searchflag, AddReadOnlyInfo, ListBrokenRefs, AppendImportedPaths)
```

```

System.object GetDependencies( 
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo,
   System.bool ListBrokenRefs,
   System.bool AppendImportedPaths
)
```

```

System.Object^ GetDependencies( 
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo,
   System.bool ListBrokenRefs,
   System.bool AppendImportedPaths
) 
```

#### Parameters

*Traverseflag*
:   True to traverse all dependency levels, false to get first level (see **Remarks**)

*Searchflag*
:   True to use the search rules to find dependencies, false to look where the documents were last saved (see **Remarks**)

*AddReadOnlyInfo*
:   True to show read-only information in the returned strings, false to not (see **Remarks**)

*ListBrokenRefs*
:   True to get broken references, false to not

*AppendImportedPaths*
:   True to append imported path names, false to not (see **Remarks**)

#### Return Value

Array of strings (see **Remarks**)

Remarks

Calling this method on a drawing document returns a list of all the parts and assemblies used in the drawing. If you set Traverseflag to true, then each of the parts within the assembly file is also returned in this array of strings.

Because a derived mirror part is generated from another part, the list of model dependencies returned by this method would include the original part used to generate the derived mirror part.

Library features are completely unassociated. They do not require the library nor do they update when changes are made to the library feature. Therefore, this method does not return library features.

If you use this method with an assembly that contains two documents, Part1 and SubAssem1, an example of what might be returned is:

[ "Part1", "C:\temp\Part1.SLDPRT", "SubAssem1", "c:\temp\SubAssem1.SLDASM" ]

If Traverseflag is set to true, then all the documents contained in SubAssem1.ASM are returned. Also, suppressed components are recognized and returned by this method as a dependent file.

If AddReadOnlyInfo is set to true, then a string of "TRUE" or "FALSE" is added to the list of strings. If Part1 and SubAssem1 are read-only, then the resulting set of strings would be:

[ "Part1", "C:\temp\Part1.SLDPRT", "TRUE", "SubAssem1", "c:\temp\SubAssem1.SLDASM", "FALSE" ]  
  
If AppendImportedPaths is set to true, and Part1 was imported, "|*imported\_file\_path*" is appended to the Part1 path. The resulting set of strings would be:

[ "Part1", "C:\temp\Part1.SLDPRT|c:\temp\Creo - Copy\table\_wf2.asm.1", "TRUE", "SubAssem1", "c:\temp\SubAssem1.SLDASM", "FALSE" ]

NOTE: For assemblies containing suppressed or lightweight components, file references (return value from this method) point to the as-saved component reference because the actual component has not been loaded into memory. Because the suppressed and lightweight components have not actually been loaded, the current search criteria has not been applied to update the file references. Setting Searchflag to true causes this method to apply the current search criteria rules to locate the particular reference and may result in a different return value. Likewise, unsuppressing or resolving these components causes the current search criteria to be applied and updates the assembly's component references in memory, if necessary.

When calling this method with Searchflag set to true, you can explicitly set the search folders first. This is important because this method uses the current SOLIDWORKS directory as its second search criteria. Because the user may have interactively opened files from some random directory, you cannot be certain the current SOLIDWORKS directory is pointing to the desired location. You may want to consider setting the search folders to that of the document being used in this method.

Example

```

'This example shows how to return all of the dependent files 
'for the specied active assembly.
```

```

'VBA
```

```

'Preconditions:
'1. Open public_documents\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\api\arm2.sldasm.
'2. Open the Immediate window.  
'3. Optionally set a breakpoint after vDepend is set so you can inspect its contents.
```

```

'Postconditions:  
'Inspect the Immediate window.
```

```

Option Explicit  
Sub main()  
    Dim swApp                   As SldWorks.SldWorks  
    Dim swModel                 As SldWorks.ModelDoc2  
    Dim vDepend                 As Variant  
    Dim i                       As Long  
      
    Set swApp = CreateObject("SldWorks.Application")  
    Set swModel = swApp.ActiveDoc  
      
    vDepend = swModel.Extension.GetDependencies(True, True, True, True, True)  
      
    Debug.Print swModel.GetPathName  
    For i = 0 To (UBound(vDepend)) / 3 - 1  
        Debug.Print "    " + vDepend(2 * i + i) + " --> Read-only: " + vDepend(2 * i + (i + 2))  
    Next i  
End Sub
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::GetNumDependencies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetNumDependencies.md)  
[ISldWorks::GetDocumentDependencies2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.md)
