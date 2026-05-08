# Depth Property (ICoreFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~Depth`

Gets or sets the depth in the specified direction of this core feature.
Gets or sets the depth in the specified direction of this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Depth( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As ICoreFeatureData
Dim Index As System.Integer
Dim value As System.Double
 
instance.Depth(Index) = value
 
value = instance.Depth(Index)
```

```

System.double Depth( 
   System.int Index
) {get; set;}
```

```

property System.double Depth {
   System.double get(System.int Index);
   void set (System.int Index, System.double value);
}
```

#### Parameters

*Index*
:   Direction to extract core as defined in [swCoreFeatureDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCoreFeatureDirection_e.html)

#### Property Value

Depth

Example

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)  
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)  
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.md)
