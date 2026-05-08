# LoadExternalReferencesInMemory Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadExternalReferencesInMemory`

Gets or sets whether to load external references in memory when opening a document.
Gets or sets whether to load external references in memory when opening a document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LoadExternalReferencesInMemory As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.LoadExternalReferencesInMemory = value
 
value = instance.LoadExternalReferencesInMemory
```

```

System.bool LoadExternalReferencesInMemory {get; set;}
```

```

property System.bool LoadExternalReferencesInMemory {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to load external references in memory, false (default) to not

Remarks

This property is:

- not valid for opening **3D**EXPERIENCE files using SOLIDWORKS Connected.

- valid only if [swUserPreferenceIntegerValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).swLoadExternalReferences is not set to [swLoadExternalReferences\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoadExternalReferences_e.html).swLoadExternalReferences\_None.

Note: The **System Options > External References > Load documents in memory only** user preference and [swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.html).swExtRefLoadRefDocsInMemory are ignored when opening documents through the API because this method and [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) ([swOpenDocOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swOpenDocOptions_e.html).swOpenDocOptions\_LoadExternalReferencesInMemory) have sole control of reference loading.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)
