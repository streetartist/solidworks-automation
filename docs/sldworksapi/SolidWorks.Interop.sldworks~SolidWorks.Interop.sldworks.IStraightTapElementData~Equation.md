# Equation Property (IStraightTapElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~Equation`

Gets or sets the equation for the blind depth or offset distance of this straight tap hole element.
Gets or sets the equation for the blind depth or offset distance of this straight tap hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Equation As System.Integer
```

```

Dim instance As IStraightTapElementData
Dim value As System.Integer
 
instance.Equation = value
 
value = instance.Equation
```

```

System.int Equation {get; set;}
```

```

property System.int Equation {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Equation for the blind depth or offset distance as defined in [swStraightTapHoleEquation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStraightTapHoleEquation_e.html)

Remarks

If [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.md) is set to false, and:

- [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.md) is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondBlind, then this property specifies the equation for the depth of the Blind end condition. If this property is set to swStraightTapeHoleEquation\_e.swStraightTapHoleEquation\_UserDefinedValue, then use [IAdvancedHoleElementData::BlindDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~BlindDepth.md) to set the custom Blind depth of this hole element.
- IAdvancedHoleElementData::EndCondition is specifically set to anything other than Blind, then this property is not valid.

If IAdvancedHoleFeatureData::UseBaselineDimensions is set to true, then:

- the end condition automatically becomes swEndConditions\_e.swEndCondOffsetFromSurface,

   - and -

- this property specifies the equation for the offset distance. If this property is set to swStraightTapHoleEquation\_e.swStraightTapHoleEquation\_UserDefinedValue, then use [IAdvancedHoleElementData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.md) to set the custom offset distance of this hole element.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md)  
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.md)
