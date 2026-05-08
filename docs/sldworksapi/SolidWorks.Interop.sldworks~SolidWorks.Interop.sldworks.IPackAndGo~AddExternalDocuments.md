# AddExternalDocuments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddExternalDocuments`

Adds non-SOLIDWORKS files to Pack and Go.
Adds non-SOLIDWORKS files to Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddExternalDocuments( _
   ByVal DocumentNames As System.Object _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean
 
value = instance.AddExternalDocuments(DocumentNames)
```

```

System.bool AddExternalDocuments( 
   System.object DocumentNames
)
```

```

System.bool AddExternalDocuments( 
   System.Object^ DocumentNames
) 
```

#### Parameters

*DocumentNames*
:   Array of paths and filenames of non-SOLIDWORKS files to add to Pack and Go

#### Return Value

True if the files are added to Pack and Go, false if not

Remarks

Duplicate files are not allowed. You can add any type of non-SOLIDWORKS file.

Example

[Add and Remove Files from Pack And Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)  
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)  
[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::GetExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetExternalDocuments.md)  
[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.md)  
[IModelDocExtension::GetRenderStockReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.md)  
[IPackAndGo::RemoveExternalDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~RemoveExternalDocuments.md)
