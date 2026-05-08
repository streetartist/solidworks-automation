# swOpenDocOptions_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swOpenDocOptions_e`

How to open documents using ISldWorks::OpenDoc6. Bitmask.
How to open documents using [ISldWorks::OpenDoc6](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html). [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("F8C30B65-20A5-4DA0-8003-D3D6C78E69C4")>
Public Enum swOpenDocOptions_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swOpenDocOptions_e
```

```

[System.Runtime.InteropServices.Guid("F8C30B65-20A5-4DA0-8003-D3D6C78E69C4")]
public enum swOpenDocOptions_e : System.Enum 
```

```

public enum swOpenDocOptions_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("F8C30B65-20A5-4DA0-8003-D3D6C78E69C4")
public enum swOpenDocOptions_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("F8C30B65-20A5-4DA0-8003-D3D6C78E69C4")]
__value public enum swOpenDocOptions_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("F8C30B65-20A5-4DA0-8003-D3D6C78E69C4")]
public enum class swOpenDocOptions_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swOpenDocOptions\_AdvancedConfig** | 8192 or 0x2000; Open assembly using an advanced configuration |
| **swOpenDocOptions\_AutoMissingConfig** | 32 or 0x20 = Obsolete; do not use  The software automatically uses the last-used configuration of a model when it discovers missing configurations or component references as it silently opens drawings and assemblies. |
| **swOpenDocOptions\_DontLoadHiddenComponents** | 256 or 0x100 = By default, hidden components are loaded when you open an assembly document. Set swOpenDocOptions\_DontLoadHiddenComponents to not load hidden components when opening an assembly document |
| **swOpenDocOptions\_LDR\_EditAssembly** | 2048 or 0x800 = Open in Large Design Review (resolved) mode with edit assembly enabled; use in combination with swOpenDocOptions\_ViewOnly |
| **swOpenDocOptions\_LoadExternalReferencesInMemory** | 512 or 0x200 = Open external references in memory only; this setting is valid only if [swUserPreferenceIntegerValue\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.md).swLoadExternalReferences is not set to [swLoadExternalReferences\_e](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swLoadExternalReferences_e.md).swLoadExternalReferences\_None  [swUserPreferenceToggle\_e.swExtRefLoadRefDocsInMemory](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceToggle_e.md) (**System Options > External References > Load documents in memory only**) is ignored when opening documents through the API because [IDocumentSpecification::LoadExternalReferencesInMemory](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~LoadExternalReferencesInMemory.html) and [ISldWorks::OpenDoc6](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) (swOpenDocOptions\_e.swOpenDocOptions\_LoadExternalReferencesInMemory) have sole control of reference loading |
| **swOpenDocOptions\_LoadLightweight** | 128 or 0x80 = Open assembly document as lightweight  NOTE: The default for whether an assembly document is opened lightweight is based on a registry setting accessed via Tools, Options, Assemblies or with the user preference setting swAutoLoadPartsLightweight    To override the default and specify a value with [ISldWorks::OpenDoc6](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html), set swOpenDocOptions\_OverrideDefaultLoadLightweight. If set, then you can set swOpenDocOptions\_LoadLightweight to open an assembly document as lightweight |
| **swOpenDocOptions\_LoadModel** | 16 or 0x10 = Load Detached model upon opening document (drawings only) |
| **swOpenDocOptions\_OpenDetailingMode** | 1024 or 0x400 = Open document in detailing mode |
| **swOpenDocOptions\_OverrideDefaultLoadLightweight** | 64 or 0x40 = Override default setting whether to open an assembly document as lightweight |
| **swOpenDocOptions\_RapidDraft** | 8 or 0x8 = Convert document to Detached format (drawings only) |
| **swOpenDocOptions\_ReadOnly** | 2 or 0x2 = Open document read only |
| **swOpenDocOptions\_Silent** | 1 or 0x1 = Open document silently |
| **swOpenDocOptions\_SpeedPak** | 4096 or 0x1000 = Open document using the SpeedPak option |
| **swOpenDocOptions\_ViewOnly** | 4 or 0x4 = Open document in Large Design Review mode (assemblies only) |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swOpenDocOptions\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
