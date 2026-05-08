# GetVisibleBox Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox`

Gets the visible bounding box set by IModelDocExtension::SetVisibleBox for a part or an assembly.
Gets the visible bounding box set by [IModelDocExtension::SetVisibleBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.md) for a part or an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleBox( _
   ByRef UpperLeft As MathPoint, _
   ByRef LowerRight As MathPoint _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim UpperLeft As MathPoint
Dim LowerRight As MathPoint
Dim value As System.Boolean
 
value = instance.GetVisibleBox(UpperLeft, LowerRight)
```

```

System.bool GetVisibleBox( 
   out MathPoint UpperLeft,
   out MathPoint LowerRight
)
```

```

System.bool GetVisibleBox( 
   [Out] MathPoint^ UpperLeft,
   [Out] MathPoint^ LowerRight
) 
```

#### Parameters

*UpperLeft*
:   Upper-left [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of the bounding box

*LowerRight*
:   Lower-right [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of the bounding box

#### Return Value

True if the bounding box was set, false if not

Remarks

SOLIDWORKS 2007 FCS, Revision Number 15.0

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.md)  
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.md)
