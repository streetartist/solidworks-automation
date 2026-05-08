# IAddHoleCallout2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddHoleCallout2`

Adds a hole callout at the specified position to the hole whose edge is selected.
Adds a hole callout at the specified position to the hole whose edge is selected.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddHoleCallout2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension
 
value = instance.IAddHoleCallout2(X, Y, Z)
```

```

DisplayDimension IAddHoleCallout2( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

DisplayDimension^ IAddHoleCallout2( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X position of hole callout in meters

*Y*
:   Y position of hole callout in meters

*Z*
:   Z position of hole callout in meters

#### Return Value

Pointer to [DisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object representing the hole callout

Remarks

When you call this method, the user must click OK in the dialog that shows the system-generated hole callout.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDisplayDimension::IsHoleCallout Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md)  
[IDrawingDoc::AddHoleCallout2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddHoleCallout2.md)  
[IDisplayDimension::GetHoleCalloutVariables Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetHoleCalloutVariables.md)
