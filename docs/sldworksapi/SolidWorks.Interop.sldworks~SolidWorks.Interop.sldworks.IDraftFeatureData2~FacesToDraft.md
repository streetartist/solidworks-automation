# FacesToDraft Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacesToDraft`

Gets or sets the faces that define this draft feature.
Gets or sets the faces that define this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FacesToDraft As System.Object
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Object
 
instance.FacesToDraft = value
 
value = instance.FacesToDraft
```

```

System.object FacesToDraft {get; set;}
```

```

property System.Object^ FacesToDraft {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::GetFacesToDraftCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetFacesToDraftCount.md)  
[IDraftFeatureData2::IGetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetFacesToDraft.md)  
[IDraftFeatureData2::ISetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.md)
