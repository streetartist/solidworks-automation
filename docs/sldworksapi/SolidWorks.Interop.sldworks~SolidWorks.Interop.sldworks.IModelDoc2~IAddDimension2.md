# IAddDimension2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDimension2`

Obsolete. Superseded by IModelDocExtension::AddDimension.
Obsolete. Superseded by [IModelDocExtension::AddDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddDimension2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As DisplayDimension
```

```

Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As DisplayDimension
 
value = instance.IAddDimension2(X, Y, Z)
```

```

DisplayDimension IAddDimension2( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

DisplayDimension^ IAddDimension2( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   :   Dimension text location in meters

*Y*
:   Dimension text location in meters

*Z*
:   Dimension text location in meters

#### Return Value

Newly created [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Remarks

You should only use this method on the visible document. Before using this method, you can check to see if the document is visible by using [ISldWorks::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md).

Dimensions are created based on selection location. For example, creating an angular dimension between two lines gets different results based on which line endpoints are selected. Therefore, if you are using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the entities for dimensioning, then you should specify the XYZ selection coordinates. You must also leave the object name argument empty, because if you pass the object name to IModelDocExtension::SelectByID2, then the selection routines tries to locate that item without using the coordinates.

Because coordinates are ignored when the object name is passed, the dimensioning routines are not able to use a specific selection location for the dimension. This causes unpredictable results in your dimension creation because you cannot be sure which line endpoint is selected by IModelDocExtension::SelectByID2.

When you use this method, you might also want to use [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) swInputDimValOnCreate to suppress the dialog box that lets the user enter the dimension value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.md)  
[IModelDoc2::AddDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.md)  
[IModelDoc2::AddHorizontalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.md)  
[IModelDoc2::AddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.md)  
[IModelDoc2::AddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddVerticalDimension2.md)  
[IModelDoc2::IAddDiameterDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDiameterDimension2.md)  
[IModelDoc2::IAddHorizontalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.md)  
[IModelDoc2::IAddRadialDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddRadialDimension2.md)  
[IModelDoc2::IAddVerticalDimension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddVerticalDimension2.md)
