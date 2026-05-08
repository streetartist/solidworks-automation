# ExcludeFromAnnotationView Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ExcludeFromAnnotationView`

Gets or sets whether to exclude BOM tables from annotation views for this SOLIDWORKS MBD 3D PDF.
Gets or sets whether to exclude BOM tables from annotation views for this SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExcludeFromAnnotationView As System.Boolean
```

```

Dim instance As IMBD3DPdfData
Dim value As System.Boolean
 
instance.ExcludeFromAnnotationView = value
 
value = instance.ExcludeFromAnnotationView
```

```

System.bool ExcludeFromAnnotationView {get; set;}
```

```

property System.bool ExcludeFromAnnotationView {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to exclude BOM tables from annotation views, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)  
[IMBD3DPdfData::GetBomAreaCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetBomAreaCount.md)  
[IMBD3DPdfData::SetBomTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetBomTable.md)
