# ChangeComponentLayer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeComponentLayer`

Puts the selected components on the specified layer.
Puts the selected components on the specified layer.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ChangeComponentLayer( _
   ByVal Layername As System.String, _
   ByVal AllViews As System.Boolean _
) 
```

```

Dim instance As IDrawingDoc
Dim Layername As System.String
Dim AllViews As System.Boolean
 
instance.ChangeComponentLayer(Layername, AllViews)
```

```

void ChangeComponentLayer( 
   System.string Layername,
   System.bool AllViews
)
```

```

void ChangeComponentLayer( 
   System.String^ Layername,
   System.bool AllViews
) 
```

#### Parameters

*Layername*
:   Name of layer for components

*AllViews*
:   True changes the component layer for all views in the drawing, false changes only the selected view

Example

[Create Layer for Selected View (VBA)](Create_Layer_for_Selected_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::OnComponentProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~OnComponentProperties.md)  
[IDrawingDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ResolveOutOfDateLightWeightComponents.md)  
[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)
