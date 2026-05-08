# Flip Property (ISurfaceOffsetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Flip`

Gets or sets the offset flip setting for this surface offset feature.
Gets or sets the offset flip setting for this surface offset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Flip As System.Boolean
```

```

Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Boolean
 
instance.Flip = value
 
value = instance.Flip
```

```

System.bool Flip {get; set;}
```

```

property System.bool Flip {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True flips the offset, false does not

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
