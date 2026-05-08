# AutoRepair Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AutoRepair`

Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened.
Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoRepair As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.AutoRepair = value
 
value = instance.AutoRepair
```

```

System.bool AutoRepair {get; set;}
```

```

property System.bool AutoRepair {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically repair custom properties errors, false to not (default) (see **Remarks**)

Remarks

This property is valid only if [IDocumentSpecification::Silent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Silent.md) is set to true.

If the document to be opened has a non-critical data error, the non-critical data error may or may not be repaired, depending on how you set this property and other conditions.

If you set this property to true, and the file to open has non-critical data corruption in:

- The custom properties area, the repair proceeds, and [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md) returns the document with warning, [swFileLoadWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html).swFileLoadWarning\_AutomaticRepair.
- An area other than custom properties, the document is not repaired.

The following files are created in c**:\Users\***user***\AppData\Local\Temp:**

- **Repaired\_*file\_name.sld\****
- **Backup of *file\_name.sld\****

If you set this property to false, and the file to open has non-critical data corruption:

- The document is not repaired.
- The document does not open.
- [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md) fails and returns null with error code, [swFileLoadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).FileRequiresAutoRepair.

If critical data corruption exists in the file, and you set [IDocumentSpecification::CriticalDataRepair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~CriticalDataRepair.md) to true to handle critical data corruption:

- Non-critical data corruptions are ignored and not repaired.
- Repairing critical errors necessitates obliterating all non-critical data.

Use For C++ only, VARIANT\_TRUE (-1) automatically repairs the file, and VARIANT\_FALSE (0) does not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
