# GetSectionedBodies Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSectionedBodies`

Gets the sectioned bodies in the specified section view.
Gets the sectioned bodies in the specified section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSectionedBodies( _
   ByVal ViewIn As System.Object _
) As System.Object
```

```

Dim instance As IComponent2
Dim ViewIn As System.Object
Dim value As System.Object
 
value = instance.GetSectionedBodies(ViewIn)
```

```

System.object GetSectionedBodies( 
   System.object ViewIn
)
```

```

System.Object^ GetSectionedBodies( 
   System.Object^ ViewIn
) 
```

#### Parameters

*ViewIn*
:   Model view displaying the sectioned view

#### Return Value

Array of the sectioned bodies in the specified view

Remarks

To determine if the model view you want is currently displaying a sectioned view, use [IModelView::GetDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.md).

If you need the full body representation, use [IComponent2::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.md), [IPartDoc::GetBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2.md), or [IPartDoc::EnumBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.md), which ignore the sectioning operation.

For COM implementations, see [IComponent2::EnumSectionedBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumSectionedBodies.md).

If a component is suppressed or lightweight, this method returns NULL because the component is not loaded into memory by SOLIDWORKS. For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

Example

[Get Sectioned Bodies (VBA)](Get_Sectioned_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
