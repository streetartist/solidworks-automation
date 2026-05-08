# InsertNewVirtualAssembly Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly`

Creates a new assembly from this assembly and saves it internally as a virtual component.
Creates a new assembly from this assembly and saves it internally as a virtual component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertNewVirtualAssembly( _
   ByRef InsertedComponent As Component2 _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim InsertedComponent As Component2
Dim value As System.Integer
 
value = instance.InsertNewVirtualAssembly(InsertedComponent)
```

```

System.int InsertNewVirtualAssembly( 
   out Component2 InsertedComponent
)
```

```

System.int InsertNewVirtualAssembly( 
   [Out] Component2^ InsertedComponent
) 
```

#### Parameters

*InsertedComponent*
:   New assembly inserted as virtual component

#### Return Value

Error code as defined by [swInsertNewPartErrorCode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewPartErrorCode_e.html)

Remarks

If nothing is pre-selected, this method inserts the virtual assembly into the main assembly. If a sub-assembly is pre-selected, it inserts the virtual assembly into the sub-assembly.

Example

[Insert New Virtual Assembly (VBA)](Insert_New_Virtual_Assembly_Example_VB.htm)  
[Insert New Virtual Assembly (VB.NET)](Insert_New_Virtual_Assembly_Example_VBNET.htm)  
[Insert New Virtual Assembly (C#)](Insert_New_Virtual_Assembly_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::InsertNewVirtualPart Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualPart.md)  
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.md)  
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.md)  
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.md)  
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.md)
