# DisplayedUnit Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~DisplayedUnit`

Gets or sets the unit type to display in this PropertyManager page number box.
Gets or sets the unit type to display in this PropertyManager page number box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayedUnit As System.Integer
```

```

Dim instance As IPropertyManagerPageNumberbox
Dim value As System.Integer
 
instance.DisplayedUnit = value
 
value = instance.DisplayedUnit
```

```

System.int DisplayedUnit {get; set;}
```

```

property System.int DisplayedUnit {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Unit type to display in this PropertyManager page number box (see **Remarks**)

Remarks

This property depends on the unit type specified for the [IPropertyManagerPageNumberbox::SetRange2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~SetRange2.md)'s Units parameter, which is a value from [swNumberboxUnitType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberboxUnitType_e.html).

|  |  |
| --- | --- |
| **If IPropertyManagerPageNumberbox::SetRange2's Units parameter is...** | **Then specifiy an enumerator from this enumeration for IPropertyManagerPageNumber::DisplayedUnit...** |
| swNumberBox\_Length | [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) |
| swNumberBox\_Angle | [swAngleUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html) |
| swNumberBox\_Force | [swUnitsForce\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUnitsForce_e.html) |
| swNumberBox\_Time | [swUnitsTimeUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUnitsTimeUnit_e.html) |

For example, IPropertyManagerPageNumberbox::DisplayedUnit allows an add-in to have a number box that shows length values in inches, even though the system default units are meters. Remember that the values specified for both [IPropertyManagerPageNumberbox::Value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox~Value.md) and IPropertyManagerPageNumberbox::SetRange2 are in system units; IPropertyManagerPageNumberbox::DisplayedUnits simply controls how that value is displayed in the PropertyManager page number box.

You can call IPropertyManagerPageNumberbox::DisplayedUnit and change the units displayed in a number box while a Propertymanager page is displayed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageNumberbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox.md)  
[IPropertyManagerPageNumberbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.md)
