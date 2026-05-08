# SetFixedFace Method (IConvertSolidFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~SetFixedFace`

Sets the face that remains in place when the part is flattened in this convert solid feature.
Sets the face that remains in place when the part is flattened in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFixedFace( _
   ByVal FaceIn As System.Object _
) 
```

```

Dim instance As IConvertSolidFeatureData
Dim FaceIn As System.Object
 
instance.SetFixedFace(FaceIn)
```

```

void SetFixedFace( 
   System.object FaceIn
)
```

```

void SetFixedFace( 
   System.Object^ FaceIn
) 
```

#### Parameters

*FaceIn*
:   [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)  
[IConvertSolidFeatureData::GetFixedFace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GetFixedFace.md)
