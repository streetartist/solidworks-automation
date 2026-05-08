# IDrawingComponent Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent`

Represents the referenced component in a drawing view.
Represents the referenced component in a drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IDrawingComponent 
```

```

Dim instance As IDrawingComponent
```

```

public interface IDrawingComponent 
```

```

public interface class IDrawingComponent 
```

Remarks

This object ties the [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) object of the [IAssemblyDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md) object with the [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object of the [IDrawingDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md) object. This functionality allows an application to manipulate the drawing-related settings of a referenced component without having to preselect that component.

Example

[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)  
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)  
[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)  
[Select Drawing Component (C#)](Select_Drawing_Component_Example_CSharp.htm)  
[Select Drawing Component (VB.NET)](Select_Drawing_Component_Example_VBNET.htm)  
[Select Drawing Component (VBA)](Select_Drawing_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
