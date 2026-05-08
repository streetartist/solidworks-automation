# CreateAttachSTEP242 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~CreateAttachSTEP242`

Gets or sets whether to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to the SOLIDWORKS MBD 3D PDF.
Gets or sets whether to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to the SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CreateAttachSTEP242 As System.Boolean
```

```

Dim instance As IMBD3DPdfData
Dim value As System.Boolean
 
instance.CreateAttachSTEP242 = value
 
value = instance.CreateAttachSTEP242
```

```

System.bool CreateAttachSTEP242 {get; set;}
```

```

property System.bool CreateAttachSTEP242 {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to SOLIDWORKS MBD 3D PDF, false to not

Example

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md) examples.

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
[IModelDocExtension::PublishSTEP242File Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishSTEP242File.md)
