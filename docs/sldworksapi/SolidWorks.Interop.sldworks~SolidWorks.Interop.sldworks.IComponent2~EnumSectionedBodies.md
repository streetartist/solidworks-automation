# EnumSectionedBodies Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumSectionedBodies`

Gets the sectioned bodies seen in the specified view and returns them in an enumerated list.
Gets the sectioned bodies seen in the specified view and returns them in an enumerated list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EnumSectionedBodies( _
   ByVal ViewIn As ModelView _
) As EnumBodies2
```

```

Dim instance As IComponent2
Dim ViewIn As ModelView
Dim value As EnumBodies2
 
value = instance.EnumSectionedBodies(ViewIn)
```

```

EnumBodies2 EnumSectionedBodies( 
   ModelView ViewIn
)
```

```

EnumBodies2^ EnumSectionedBodies( 
   ModelView^ ViewIn
) 
```

#### Parameters

*ViewIn*
:   Pointer to the [model view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md) displaying the sectioned view

#### Return Value

Pointer to the [enumerated list of bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2.md)

Remarks

To determine if the model view you want is currently displaying a sectioned view, use [IModelView::GetDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.md).

If you need the full body representation, use [IComponent2::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.md), [IPartDoc::GetBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2.md), or [IPartDoc::EnumBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.md), which ignore the sectioning operation.

For Dispatch implementations, see [IComponent2::GetSectionedBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSectionedBodies.md).

If a component is suppressed or lightweight, this method returns NULL because the component is not loaded into memory by SOLIDWORKS. For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
