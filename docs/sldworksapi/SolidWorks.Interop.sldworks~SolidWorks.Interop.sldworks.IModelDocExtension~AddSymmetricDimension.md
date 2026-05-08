# AddSymmetricDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSymmetricDimension`

Creates a full symmetrical angular dimension at the specified location for the selected entities.
Creates a full symmetrical angular dimension at the specified location for the selected entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSymmetricDimension( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.AddSymmetricDimension(X, Y, Z)
```

```

System.object AddSymmetricDimension( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ AddSymmetricDimension( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X coordinate of the symmetrical angular dimension

*Y*
:   Y coordinate of the symmetrical angular dimension

*Z*
:   Z coordinate of the symmetrical angular dimension

#### Return Value

Symmetrical angular [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)

Remarks

This type of dimensioning is helpful when you create a sketch for revolved geometry that requires a full angular dimension.

Before calling this method, you might want to call [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) with [swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swInputDimValOnCreate to suppress the dialog box that allows the user to enter the dimension value.

Example

[Create Full Symmetrical Angular Dimension (C#)](Create_Full_Symmetrical_Angular_Dimension_Example_CSharp.htm)  
[Create Full Symmetrical Angular Dimension (VB.NET)](Create_Full_Symmetrical_Angular_Dimension_Example_VBNET.htm)  
[Create Full Symmetrical Angular Dimension (VBA)](Create_Full_Symmetrical_Angular_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::AddDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.md)  
[IModelDoc2::AddDiameterDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDiameterDimension2.md)  
[IModelDoc2::IAddDiameterDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddDiameterDimension2.md)  
[IModelDoc2::AddHorizontalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddHorizontalDimension2.md)  
[IModelDoc2::IAddHorizontalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddHorizontalDimension2.md)  
[IModelDoc2::AddRadialDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddRadialDimension2.md)  
[IModelDoc2::IAddRadialDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddRadialDimension2.md)  
[IModelDoc2::AddVerticalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddVerticalDimension2.md)  
[IModelDoc2::IAddVerticalDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddVerticalDimension2.md)  
[IModelDocExtension::AddSpecificDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddSpecificDimension.md)
