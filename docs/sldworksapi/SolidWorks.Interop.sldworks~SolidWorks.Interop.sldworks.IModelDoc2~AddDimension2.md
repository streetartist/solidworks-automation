# AddDimension2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2`

Creates a display dimension at the specified location for selected entities.
Creates a display dimension at the specified location for selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddDimension2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.AddDimension2(X, Y, Z)
```

```

System.object AddDimension2( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ AddDimension2( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   Dimension text location in meters

*Y*
:   Dimension text location in meters

*Z*
:   Dimension text location in meters

#### Return Value

Newly created [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Remarks

Before calling this method, you must select the entities for which to add a display dimension.

If extension lines are needed during dimensioning because the selected entities do not unambiguously define what needs to be dimensioned, call [IModelDocExtension::AddDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.md) instead of this method.

To dimension, make selections based on location and not name. For example, creating an angular dimension between two lines gets different results based on which line endpoints are selected. Therefore, if you are using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the entities for dimensioning, then you should specify the X, Y,  and Z selection coordinates. You must also leave the object name argument empty, because if you pass the object name to IModelDocExtension::SelectByID2, then the selection routines use the object name instead of the coordinates to locate that item.

**NOTE:** To change the angle in an angular dimension to its supplementary angle, use [IDisplayDimension::SupplementaryAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SupplementaryAngle.md).

Because coordinates are ignored when the object name is passed, the dimensioning routines are not able to use a specific selection location for the dimension. This causes unpredictable results during dimension creation. IModelDocExtension::SelectByID2 randomly selects the line endpoint.

You should only use this method on visible documents. Before using this method, check to see if the document is visible by using [ISldWorks::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md).

When you use this method, you might also want to use [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) with swInputDimValOnCreate to suppress the dialog box that lets the user type a dimension value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IAddDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDimension2.md)  
[IModelDoc2::IAddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDiameterDimension2.md)  
[IModelDoc2::IAddHorizontalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.md)  
[IModelDoc2::IAddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddRadialDimension2.md)  
[IModelDoc2::IAddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddVerticalDimension2.md)  
[IModelDoc2::AddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.md)  
[IModelDoc2::AddHorizontalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.md)  
[IModelDoc2::AddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.md)  
[IModelDoc2::AddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddVerticalDimension2.md)  
[IModelDocExtension::AddSpecificDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.md)  
[IDrawingDoc::InsertChainDim Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertChainDim.md)
