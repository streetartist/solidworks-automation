# CompressLossyTessellation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CompressLossyTessellation`

Gets or sets whether to apply lossy compression to polygons in the model when publishing to SOLIDWORKS MBD 3D PDF.
Gets or sets whether to apply lossy compression to polygons in the model when publishing to SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CompressLossyTessellation As System.Boolean
```

```

Dim instance As IMBD3DPdfData
Dim value As System.Boolean
 
instance.CompressLossyTessellation = value
 
value = instance.CompressLossyTessellation
```

```

System.bool CompressLossyTessellation {get; set;}
```

```

property System.bool CompressLossyTessellation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to apply lossy compression to polygons in the model, false to not

Example

[Attach Files to MBD 3D PDF (C#)](Attach_Files_to_MBD_3D_PDF_Example_CSharp.htm)  
[Attach Files to MBD 3D PDF (VB.NET)](Attach_Files_to_MBD_3D_PDF_Example_VBNET.htm)  
[Attach Files to MBD 3D PDF (VBA)](Attach_Files_to_MBD_3D_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)  
[IMBD3DPdfData::Accuracy Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~Accuracy.md)
