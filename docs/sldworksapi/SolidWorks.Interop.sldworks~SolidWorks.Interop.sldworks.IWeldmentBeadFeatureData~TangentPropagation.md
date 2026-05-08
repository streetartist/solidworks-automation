# TangentPropagation Property (IWeldmentBeadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~TangentPropagation`

Gets or sets whether to propagate the weld bead along the tangent.
Gets or sets whether to propagate the weld bead along the tangent.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TangentPropagation As System.Boolean
```

```

Dim instance As IWeldmentBeadFeatureData
Dim value As System.Boolean
 
instance.TangentPropagation = value
 
value = instance.TangentPropagation
```

```

System.bool TangentPropagation {get; set;}
```

```

property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate the weld bead along the tangent, false to not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.md)  
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.md)  
[IWeldmentBeadFeatureData::BeadLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadLength.md)  
[IWeldmentBeadFeatureData::BeadPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadPitch.md)
