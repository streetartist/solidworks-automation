# RevolutionType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionType`

Gets or sets the type of revolution to specify for this screw mate.
Gets or sets the type of revolution to specify for this screw mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RevolutionType As System.Integer
```

```

Dim instance As IScrewMateFeatureData
Dim value As System.Integer
 
instance.RevolutionType = value
 
value = instance.RevolutionType
```

```

System.int RevolutionType {get; set;}
```

```

property System.int RevolutionType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of revolution as defined in [swScrewMateDistanceOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swScrewMateDistanceOptions_e.html)

Remarks

If you set this property to swScrewMateDistanceOptions\_e:

- swDistancePerRevolution, then specify [IScrewMateFeatureData::RevolutionVal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData~RevolutionVal.md) with the distance that one component translates for each revolution of the other component.
- swRevolutionsPerUnitLength, then specify IScrewMateFeatureData::RevolutionVal with the number of revolutions of one component for each unit length that the other component translates.

Example

See the [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScrewMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.md)  
[IScrewMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.md)
