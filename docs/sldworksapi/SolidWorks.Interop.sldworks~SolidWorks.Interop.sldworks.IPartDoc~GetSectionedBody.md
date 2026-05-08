# GetSectionedBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetSectionedBody`

Gets the sectioned body seen in the specified drawing view.
Gets the sectioned body seen in the specified drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSectionedBody( _
   ByVal ViewIn As System.Object _
) As System.Object
```

```

Dim instance As IPartDoc
Dim ViewIn As System.Object
Dim value As System.Object
 
value = instance.GetSectionedBody(ViewIn)
```

```

System.object GetSectionedBody( 
   System.object ViewIn
)
```

```

System.Object^ GetSectionedBody( 
   System.Object^ ViewIn
) 
```

#### Parameters

*ViewIn*
:   [Model view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)

#### Return Value

[Sectioned body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

To determine if the desired model view is currently displaying a sectioned view, use  [IModelView::GetDisplayState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.md).

If you need the full body representation, use [IPartDoc::GetBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetBodies2.md) or [IPartDoc::EnumBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.md), which ignores the sectioning operation.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::IGetSectionedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetSectionedBody2.md)
