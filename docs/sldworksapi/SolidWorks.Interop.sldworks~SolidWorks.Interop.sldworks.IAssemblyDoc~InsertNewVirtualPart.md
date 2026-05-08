# InsertNewVirtualPart Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualPart`

Creates a new part in the context of an assembly and saves the part internally in the assembly file as a virtual component.
Creates a new part in the context of an assembly and saves the part internally in the assembly file as a virtual component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertNewVirtualPart( _
   ByVal FaceOrPlaneToSelect As System.Object, _
   ByRef InsertedComponent As Component2 _
) As System.Integer
```

```

Dim instance As IAssemblyDoc
Dim FaceOrPlaneToSelect As System.Object
Dim InsertedComponent As Component2
Dim value As System.Integer
 
value = instance.InsertNewVirtualPart(FaceOrPlaneToSelect, InsertedComponent)
```

```

System.int InsertNewVirtualPart( 
   System.object FaceOrPlaneToSelect,
   out Component2 InsertedComponent
)
```

```

System.int InsertNewVirtualPart( 
   System.Object^ FaceOrPlaneToSelect,
   [Out] Component2^ InsertedComponent
) 
```

#### Parameters

*FaceOrPlaneToSelect*
:   Plane or planar face

*InsertedComponent*
:   New part inserted as virtual component

#### Return Value

Error as defined by [swInsertNewPartErrorCode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewPartErrorCode_e.html)

Example

[Insert New Virtual Component (VB.NET)](Insert_New_Virtual_Component_Example_VBNET.htm)  
[Insert New Virtual Component (VBA)](Insert_New_Virtual_Component_Example_VB.htm)  
[Insert New Virtual Component (C#)](Insert_New_Virtual_Component_Example_CSharp.htm)  
[Insert New Instance of Virtual Component (VBA)](Insert_New_Instance_of_Virtual_Component_Example_VB.htm)  
[Insert New Instance of Virtual Component (VB.NET)](Insert_New_Instance_of_Virtual_Component_Example_VBNET.htm)  
[Insert New Instance of Virtual Component (C#)](Insert_New_Instance_of_Virtual_Component_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.md)  
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.md)  
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.md)  
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.md)  
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.md)
