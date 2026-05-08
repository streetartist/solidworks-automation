# ReverseDirection Property (ISimpleHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReverseDirection`

Gets or sets whether to reverse the direction of the cut.
Gets or sets whether to reverse the direction of the cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseDirection As System.Boolean
```

```

Dim instance As ISimpleHoleFeatureData2
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

True reverses the direction of the cut, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md)  
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.md)  
[ISimpleHoleFeatureData2::GetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetDirectionReference.md)  
[ISimpleHoleFeatureData2::SetDirectionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SetDirectionReference.md)
