# ReverseDirection Property (IPrimaryMemberPointLengthFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~ReverseDirection`

Gets and sets whether to reverse the length of this structure system member.
Gets and sets whether to reverse the length of this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseDirection As System.Boolean
```

```

Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Boolean
 
instance.ReverseDirection = value
 
value = instance.ReverseDirection
```

```

System.bool ReverseDirection {get; set;}
```

```

property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the member direction, false to not

Remarks

This property is valid only if [IPrimaryMemberPointLengthFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.md) is [swPrimaryMemberPointLengthEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html).swPrimaryMemberPointLengthEndCondition\_Length.

Example

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md)  
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.md)
