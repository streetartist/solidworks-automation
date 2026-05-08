# IAssemblyDoc Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc`

Allows access to functions that perform assembly operations; for example, adding new components, adding mate conditions, hiding, and exploding components.
Allows access to functions that perform assembly operations; for example, adding new components, adding mate conditions, hiding, and exploding components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IAssemblyDoc 
```

```

Dim instance As IAssemblyDoc
```

```

public interface IAssemblyDoc 
```

```

public interface class IAssemblyDoc 
```

Remarks

The SOLIDWORKS API includes functions that are common to all document types; for example, determining the file name associated with a document is a common operation. To expose common document-level functions, the SOLIDWORKS API uses the [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) object.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md) topic for a list of delegates for this interface.

Example

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)  
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)  
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)  
[Insert and Save Virtual Assembly (C#)](Insert_and_Save_Virtual_Assembly_Example_CSharp.htm)  
[Insert and Save Virtual Assembly (VB.NET)](Insert_and_Save_Virtual_Assembly_Example_VBNET.htm)  
[Insert and Save Virtual Assembly (VBA)](Insert_and_Save_Virtual_Assembly_Example_VB.htm)  
[Add Components (C#)](Add_Components_Example_CSharp.htm)  
[Add Components (VB.NET)](Add_Components_Example_VBNET.htm)  
[Add Components (VBA)](Add_Components_Example_VB.htm)  
[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)  
[Add Component and Mate (VBA)](Add_Component_and_Mate_Example_VB.htm)  
[Insert MidSurface in Assembly (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)  
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)  
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)  
[Create Auto Route (VBA)](Create_Auto_Route_Example_VB.htm)  
[Create Auto Route (VB.NET)](Create_Auto_Route_Example_VBNET.htm)  
[Create Auto Route (C#)](Create_Auto_Route_Example_CSharp.htm)  
[Add Component and Mate (VB.NET)](Add_Component_and_Mate_Example_VBNET.htm)  
[Add Component and Mate Example (C#)](Add_Component_and_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
