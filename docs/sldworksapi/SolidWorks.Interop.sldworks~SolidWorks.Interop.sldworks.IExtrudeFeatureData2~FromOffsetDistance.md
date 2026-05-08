# FromOffsetDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetDistance`

Gets or sets the offset distance if IExtrudeFeatureData2::FromType is swExtrudeFrom_Offset.
Gets or sets the offset distance if [IExtrudeFeatureData2::FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md) is swExtrudeFrom\_Offset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FromOffsetDistance As System.Double
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Double
 
instance.FromOffsetDistance = value
 
value = instance.FromOffsetDistance
```

```

System.double FromOffsetDistance {get; set;}
```

```

property System.double FromOffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Offset distance

Example

[Create Extruded Thin Feature (VBA)](Create_Extruded_Thin_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::FromOffsetReverse Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromOffsetReverse.md)  
[IExtrudeFeatureData2::GetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetReverseOffset.md)  
[IExtrudeFeatureData2::SetReverseOffset Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetReverseOffset.md)  
[IExtrudeFeatureData2::SetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetTranslateSurface.md)  
[IExtrudeFeatureData2::GetTranslateSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetTranslateSurface.md)
