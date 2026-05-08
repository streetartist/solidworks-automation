# EndCondition Property (IAdvancedHoleElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition`

Gets or sets the end condition for this Advanced Hole element.
Gets or sets the end condition for this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndCondition As System.Integer
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.Integer
 
instance.EndCondition = value
 
value = instance.EndCondition
```

```

System.int EndCondition {get; set;}
```

```

property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

End condition (see **Remarks**)

Remarks

Valid end conditions for the Advanced Hole as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html):

- swEndCondBlind
- swEndCondThroughAll
- swEndCondUpToNext
- swEndCondOffsetFromSurface
- swEndCondUpToSelection

This property can be set for a given hole element only when its corresponding override property is set to true:

- [ICounterboreElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~EndConditionOverride.md)
- [ICountersinkElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~EndConditionOverride.md)
- [ITaperedTapElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~EndConditionOverride.md)

    - and -

- [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.md) is set to false.

Example

See the [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)  
[IStraightTapElementData::Equation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~Equation.md)  
[IAdvancedHoleElementData::OffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.md)  
[IAdvancedHoleElementData::OffsetReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetReverseDirection.md)
