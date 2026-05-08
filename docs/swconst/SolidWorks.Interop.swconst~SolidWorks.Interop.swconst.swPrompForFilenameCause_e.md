# swPrompForFilenameCause_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrompForFilenameCause_e`

Reasons for opening or saving missing dependent documents.
Reasons for opening or saving missing dependent documents.

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

<System.Runtime.InteropServices.GuidAttribute("8D280B53-110E-461C-A46B-ED24EC9E0BE9")>
Public Enum swPrompForFilenameCause_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPrompForFilenameCause_e
```

```

[System.Runtime.InteropServices.Guid("8D280B53-110E-461C-A46B-ED24EC9E0BE9")]
public enum swPrompForFilenameCause_e : System.Enum 
```

```

public enum swPrompForFilenameCause_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("8D280B53-110E-461C-A46B-ED24EC9E0BE9")
public enum swPrompForFilenameCause_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("8D280B53-110E-461C-A46B-ED24EC9E0BE9")]
__value public enum swPrompForFilenameCause_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("8D280B53-110E-461C-A46B-ED24EC9E0BE9")]
public enum class swPrompForFilenameCause_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAddComponent** | 15 |
| **swAddVirtualComponent** | 24 |
| **swComponentPropsReplace** | 10 |
| **swCreateNamedViewFromFile** | 9 |
| **swDerivedPart** | 4 |
| **swDrawingAddViewFromFile** | 13 |
| **swDrawingInsert3ViewFromFile** | 14 |
| **swEditReadOnlyComponent** | 19 = User attempted to edit a read-only component document in context. |
| **swFileReloadReplace** | 12 |
| **swFormNewSubAssembly** | 23 = For use with ISldWorks [PromptForFileNameNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.html) event handler, which fires the event when an interactive user wants to form a new sub-assembly. |
| **swGeneric** | 1 |
| **swInsertBlock** | 20 =  For use with ISldWorks [PromptForFileNameNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.html) event handler, which fires the event when an interactive user clicks the Browse button on the Insert Block PropertyManager page. |
| **swInsertEnvelopeFromFile** | 7 |
| **swMakeComponentIndependent** | 25 |
| **swMirrorComponent** | 2 |
| **swMirrorComponentBrowse** | 8 |
| **swOpenAssociatedDrawing** | 11 |
| **swPromptForFilename\_Cancelled** | 26 |
| **swSaveDefeaturedModel** | 22 = For use with ISldWorks [PromptForFileNameNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.html) event handler, which fires the event when an interactive user wants to save a de-featured model as a separate file. |
| **swSaveRoutePart** | 17 |
| **swSaveVirtualComponentExternally** | 18 = For use with the ISldWorks [PromptForMultipleFilenamesNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForMultipleFileNamesNotifyEventHandler.html) event handler and [ISldWorks::SetMultipleFilenamesPrompt](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetMultipleFilenamesPrompt.html) to:   1. Supply path names for virtual components to be saved externally. 2. Suppress dialogs prompting user to select paths for virtual components. |
| **swSketchBlock** | 21 = For use with ISldWorks [PromptForFileNameNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_PromptForFilenameNotifyEventHandler.html) event handler, which fires the event when an interactive user clicks the Browse button on the Insert Block PropertyManager page. |
| **swSplitAssembly** | 5 |
| **swSplitPart** | 6 |
| **swStartRouteAssembly** | 16 |
| **swUnused** | 0 |
| **swWeldBead** | 3 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPrompForFilenameCause\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
