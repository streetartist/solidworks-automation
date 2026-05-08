# InsertNewAssembly Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly`

Creates a new virtual sub-assembly and optionally saves it to the specified file.
Creates a new virtual sub-assembly and optionally saves it to the specified file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertNewAssembly( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim value As System.Integer
 
value = instance.InsertNewAssembly(FileName)
```

```

System.int InsertNewAssembly( 
   System.string FileName
)
```

```

System.int InsertNewAssembly( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Full pathname of new sub-assembly document (**see Remarks**)

#### Return Value

Error code as defined by [swInsertNewAssemblyErrorCode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewAssemblyErrorCode_e.html)

Remarks

If **Tools > Options > System Options > Assemblies > Save new components to external files** is:

- selected, then this API creates a virtual sub-assembly and saves it to the file specified in FileName.
- not selected, then this API ignores FileName, does not save the sub-assembly, and creates only a virtual sub-assembly in the FeatureManager design tree.

Example

[Insert and Save Virtual Assembly (C#)](Insert_and_Save_Virtual_Assembly_Example_CSharp.htm)  
[Insert and Save Virtual Assembly (VB.NET)](Insert_and_Save_Virtual_Assembly_Example_VBNET.htm)  
[Insert and Save Virtual Assembly (VBA)](Insert_and_Save_Virtual_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.md)  
[IComponent2::SaveVirtualComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SaveVirtualComponent.md)  
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.md)  
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.md)
