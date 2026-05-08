# RevolutionVal Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionVal`

Gets or sets either the number of revolutions one component makes for each unit length that the other component translates or the distance that one component translates for each revolution of the other component.
Gets or sets either the number of revolutions one component makes for each unit length that the other component translates or the distance that one component translates for each revolution of the other component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RevolutionVal As System.Double
```

```

Dim instance As IScrewMateFeatureData
Dim value As System.Double
 
instance.RevolutionVal = value
 
value = instance.RevolutionVal
```

```

System.double RevolutionVal {get; set;}
```

```

property System.double RevolutionVal {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Revolution value (see **Remarks**)

Remarks

If [IScrewMateFeatureData::RevolutionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionType.md) is set to [swScrewMateDistanceOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swScrewMateDistanceOptions_e.html):

- swDistancePerRevolution, then specify this property with the distance that one component translates for each revolution of the other component.
- swRevolutionsPerUnitLength, then specify this property with the number of revolutions of one component for each unit length that the other component translates. Set [swUserPreferencesIntegerValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).swUnitsLinear to a unit length as defined in [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLengthUnit_e.html).

Example

See the [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md)  
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.md)
