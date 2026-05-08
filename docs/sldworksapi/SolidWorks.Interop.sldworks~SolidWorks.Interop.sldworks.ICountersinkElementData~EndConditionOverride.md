# EndConditionOverride Property (ICountersinkElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData~EndConditionOverride`

Gets or sets whether to override the end condition of this countersink hole element.
Gets or sets whether to override the end condition of this countersink hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndConditionOverride As System.Boolean
```

```

Dim instance As ICountersinkElementData
Dim value As System.Boolean
 
instance.EndConditionOverride = value
 
value = instance.EndConditionOverride
```

```

System.bool EndConditionOverride {get; set;}
```

```

property System.bool EndConditionOverride {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the end condition, false to not (see **Remarks**)

Remarks

This property can be set only if [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.md) is set to false.

Set this property to true and specify [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.md) to override the end condition.

Example

See the [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICountersinkElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.md)  
[ICountersinkElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData_members.md)
