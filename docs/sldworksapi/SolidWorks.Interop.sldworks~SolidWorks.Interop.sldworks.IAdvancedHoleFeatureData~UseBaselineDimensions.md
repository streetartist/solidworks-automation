# UseBaselineDimensions Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions`

Gets or sets whether to use baseline dimensions in this Advanced Hole.
Gets or sets whether to use baseline dimensions in this Advanced Hole.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseBaselineDimensions As System.Boolean
```

```

Dim instance As IAdvancedHoleFeatureData
Dim value As System.Boolean
 
instance.UseBaselineDimensions = value
 
value = instance.UseBaselineDimensions
```

```

System.bool UseBaselineDimensions {get; set;}
```

```

property System.bool UseBaselineDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use baseline dimensions, false to not (see **Remarks**)

Remarks

If you set this property to true, then you can get and set:

- [ICounterboreElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~UseStandardDepth.md)
- [ICountersinkElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~UseStandardDepth.md)
- [ITaperedTapElementData::UseStandardDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~UseStandardDepth.md)
- [IStraightTapElementData::Equation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~Equation.md) (for the Offset From Surface end condition only)

but you cannot set any end conditions or end condition overrides.

If you set this property to false, then the UseStandardDepth properties above are not valid, but you can get and set:

- [ICounterboreElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~EndConditionOverride.md)
- [ICountersinkElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~EndConditionOverride.md)
- [ITaperedTapElementData::EndConditionOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~EndConditionOverride.md)
- [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.md) (only if the corresponding EndConditionOverride for the element is set to true)
- [IAdvancedHoleElementData::BlindDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~BlindDepth.md) (for the Blind end condition only)
- IStraightTapElementData::Equation (for the Blind end condition only)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md)  
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.md)
