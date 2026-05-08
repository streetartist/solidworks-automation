# Entities Property (ISurfaceOffsetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Entities`

Gets or sets the offset surfaces and faces of this surface offset feature.
Gets or sets the offset surfaces and faces of this surface offset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Entities As System.Object
```

```

Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Object
 
instance.Entities = value
 
value = instance.Entities
```

```

System.object Entities {get; set;}
```

```

property System.Object^ Entities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of offset surface or face feature [entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)  
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)  
[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.md)  
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.md)  
[ISurfaceOffsetFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetEntitiesCount.md)  
[ISurfaceOffsetFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetEntities.md)  
[ISurfaceOffsetFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetEntities.md)
