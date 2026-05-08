# IGetDocumentDependencies2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2`

Gets all of the model dependencies for a document.
Gets all of the model dependencies for a document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDocumentDependencies2( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean _
) As System.String
```

```

Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim value As System.String
 
value = instance.IGetDocumentDependencies2(Document, Traverseflag, Searchflag, AddReadOnlyInfo)
```

```

System.string IGetDocumentDependencies2( 
   System.string Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

```

System.String^ IGetDocumentDependencies2( 
   System.String^ Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
) 
```

#### Parameters

*Document*
:   Name of the document

*Traverseflag*
:   True if you want to traverse down into all dependent files, false if you want only the highest level within the dependencies

*Searchflag*
:   Set this argument to True if you want to use the search rules to find dependencies, false looks where the documents were last saved

*AddReadOnlyInfo*
:   True if you wish to have read-only information with the filenames; false if not

#### Return Value

- in-process, unmanaged C++: Pointer to an array of strings with two strings for each document returned in this list of dependent files:
  - File name
  - Filename with the complete pathname; this combination repeats itself for each dependent file found for this document
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [ISldWorks::IGetDoucmentDependenciesCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2.md) to determine the size of the returned arrayl

As an example, calling this method on a drawing document returns a list of all the part and assemblies used in the drawing. If you set the Traverseflag to True, then each of the parts within the assembly file are also returned in this array of strings.

Another example would be calling this method with a derived mirror part. Because a derived mirror part is generated from another part, the list of model dependencies returned by this method would include the original part used to generate the derived mirror part.

Be aware that Library features are completely unassociated. They do not require the library nor do they update when changes are made to the Library feature. Therefore, this method would not return Library features.

If you use this method with an assembly that contains two documents, Part1 and SubAssem1, an example of what might be returned is:

[ "Part1", "C:\temp\Part1.SLDPRT", "SubAssem1", "c:\temp\SubAssem1.SLDASM" ]

If Traverseflag is set to True, then all of the documents contained in SubAssem1.ASM are also returned. Suppressed components are recognized and returned by this method as a dependent file.

If the AddReadOnlyInfo flag is set to True, then a string of "Read-Only" is added to the list of strings. If Part1 from were read-only, then the resulting set of strings would be:

[ "Part1", "C:\temp\Part1.SLDPRT", "Read-Only", "SubAssem1", "c:\temp\SubAssem1.SLDASM", "" ]

NOTE: If the SearchFlag is set to True, then the current directory is set to the directory of the document file. This replicates the interactive behavior of the References button in the File Open dialog window.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.md)
