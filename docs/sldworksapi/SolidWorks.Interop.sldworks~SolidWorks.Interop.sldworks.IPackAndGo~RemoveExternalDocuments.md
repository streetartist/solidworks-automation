# RemoveExternalDocuments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~RemoveExternalDocuments`

Removes the specified non-SOLIDWORKS files from Pack and Go.
Removes the specified non-SOLIDWORKS files from Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveExternalDocuments( _
   ByVal DocumentNames As System.Object _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean
 
value = instance.RemoveExternalDocuments(DocumentNames)
```

```

System.bool RemoveExternalDocuments( 
   System.object DocumentNames
)
```

```

System.bool RemoveExternalDocuments( 
   System.Object^ DocumentNames
) 
```

#### Parameters

*DocumentNames*
:   Array of the paths and filenames of the non-SOLIDWORKS files to remove from Pack and Go

#### Return Value

True if all of the specified non-SOLIDWORKS files are removed from Pack and Go, false if not

Remarks

In C# applications, you must wrap the array of objects for the DocumentNames parameter using the .NET Framework BStrWrapper class.

Example

[Add and Remove Files from Pack and Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)  
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)  
[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::AddExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddExternalDocuments.md)  
[IPackAndGo::GetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.md)  
[IPackAndGo::GetDocumentNamesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.md)  
[IPackAndGo::IGetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.md)
