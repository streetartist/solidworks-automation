# SolidForTrim Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SolidForTrim`

Gets or sets whether a surface trim feature is a solid body or a surface body.
Gets or sets whether a [surface trim feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.md) is a solid body or a surface body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SolidForTrim As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.SolidForTrim = value
 
value = instance.SolidForTrim
```

```

System.bool SolidForTrim {get; set;}
```

```

property System.bool SolidForTrim {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if a solid body, false if a surface body (see **Remarks**)

Remarks

This property is only available when creating a surface trim feature. Call this property:

- after calling [IFeatureManager::PreTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreTrimSurface.md)
- before calling [IFeatureManager::PostTrimSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostTrimSurface.md).

Example

[Create Solid Body Surface Trim Feature (C#)](Create_Solid_Body_Surface_Trim_Feature_Example_CSharp.htm)  
[Create Solid Body Surface Trim Feature (VB.NET)](Create_Solid_Body_Surface_Trim_Feature_Example_VBNET.htm)  
[Create Solid Body Surface Trim Feature (VBA)](Create_Solid_Body_Surface_Trim_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
