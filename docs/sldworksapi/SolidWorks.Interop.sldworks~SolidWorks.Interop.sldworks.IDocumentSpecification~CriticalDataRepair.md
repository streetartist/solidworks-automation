# CriticalDataRepair Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~CriticalDataRepair`

Gets or sets whether to automatically repair critical data errors in the file to be opened.
Gets or sets whether to automatically repair critical data errors in the file to be opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CriticalDataRepair As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.CriticalDataRepair = value
 
value = instance.CriticalDataRepair
```

```

System.bool CriticalDataRepair {get; set;}
```

```

property System.bool CriticalDataRepair {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically repair critical data errors, false to not

Remarks

This property is valid only if [IDocumentSpecification::Silent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.md) is set to true.

If you set this property to true, and the file to open has critical data corruption:

- Critical data repair proceeds.
- [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md) returns the document with warning, [swFileLoadWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html).swFileLoadWarning\_CriticalDataRepair.
- All non-critical data errors are ignored, because repairing critical errors obliterates all non-critical data in the file.

If set to true, this property instructs SOLIDWORKS to repair critical data by importing Parasolid bodies into a new file. The repaired file contains only Parasolid bodies.

The following files are created in c**:\Users\***user***\AppData\Local\Temp:**

- **Repaired\_*file\_name.sld\****
- **Backup of *file\_name.sld\****

If you set this property to false, and the file to open has critical data corruption:

- The document does not open.
- ISldWorks::OpenDoc7 fails and returns null with error code, [swFileLoadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).FileRequiresCriticalDataRepair.

Use [IDocumentSpecification::AutoRepair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair.md) to handle non-critical data corruption of files.

For C++ only, VARIANT\_TRUE (-1) automatically repairs the file, and VARIANT\_FALSE (0) does not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
