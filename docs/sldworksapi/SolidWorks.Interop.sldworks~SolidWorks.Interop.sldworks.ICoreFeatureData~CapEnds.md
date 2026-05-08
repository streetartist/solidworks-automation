# CapEnds Property (ICoreFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~CapEnds`

Gets or sets whether the endd are capped on this core feature.
Gets or sets whether the endd are capped on this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CapEnds As System.Boolean
```

```

Dim instance As ICoreFeatureData
Dim value As System.Boolean
 
instance.CapEnds = value
 
value = instance.CapEnds
```

```

System.bool CapEnds {get; set;}
```

```

property System.bool CapEnds {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if ends are capped, false if not

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
