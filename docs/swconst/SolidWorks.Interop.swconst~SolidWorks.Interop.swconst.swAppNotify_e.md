# swAppNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppNotify_e`

Application notifications.
Application notifications.

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

<System.Runtime.InteropServices.GuidAttribute("52B3516D-F2EF-4B84-83A8-B1CB93F6C772")>
Public Enum swAppNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swAppNotify_e
```

```

[System.Runtime.InteropServices.Guid("52B3516D-F2EF-4B84-83A8-B1CB93F6C772")]
public enum swAppNotify_e : System.Enum 
```

```

public enum swAppNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("52B3516D-F2EF-4B84-83A8-B1CB93F6C772")
public enum swAppNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("52B3516D-F2EF-4B84-83A8-B1CB93F6C772")]
__value public enum swAppNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("52B3516D-F2EF-4B84-83A8-B1CB93F6C772")]
public enum class swAppNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swAppActiveDocChangeNotify** | 4 = [ActiveDocChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_ActiveDocChangeNotifyEventHandler.html) |
| **swAppActiveModelDocChangeNotify** | 5 = [ActiveModelDocChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_ActiveModelDocChangeNotifyEventHandler.html) |
| **swAppBackgroundProcessingEndNotify** | 34 = [BackgroundProcessingEndNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_BackgroundProcessingEndNotifyEventHandler.html) |
| **swAppBackgroundProcessingStartNotify** | 33 = [BackgroundProcessingStartNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_BackgroundProcessingStartNotifyEventHandler.html) |
| **swAppBegin3DInterconnectTranslationNotify** | 37 = [Begin3DInterconnectTranslationNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_Begin3DinterconnectTranslationNotifyEventHandler.html) |
| **swAppBeginRecordNotify** | 24 = Not used. |
| **swAppBeginTranslationNotify** | 16 = [BeginTranslationNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_BeginTranslationNotifyEventHandler.html) |
| **swAppCommandCloseNotify** | 29 = [CommandCloseNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_CommandCloseNotifyEventHandler.html) |
| **swAppCommandOpenPreNotify** | 31 = [CommandOpenPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_CommandOpenPreNotifyEventHandler.html) |
| **swAppDestroyNotify** | 3 = [DestroyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_DestroyNotifyEventHandler.html) |
| **swAppDisplayPaneActivationNotify** | 45 = [DisplayPaneActivationNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_DisplayPaneActivationNotifyEventHandler.html) |
| **swAppDocumentConversionNotify** | 9 = [DocumentConversionNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_DocumentConversionNotifyEventHandler.html) |
| **swAppDocumentLoadNotify** | 27 = Obsolete |
| **swAppDocumentLoadNotify2** | 28 = [DocumentLoadNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_DocumentLoadNotify2EventHandler.html) |
| **swAppEnd3DInterconnectTranslationNotify** | 38 = [End3DInterconnectTranslationNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_End3DinterconnectTranslationNotifyEventHandler.html) |
| **swAppEndRecordNotify** | 25 = Not used. |
| **swAppEndTranslationNotify** | 16 = [EndTranslationNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_EndTranslationNotifyEventHandler.html) |
| **swAppFileCloseNotify** | 32 = [FileCloseNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_FileCloseNotifyEventHandler.html) |
| **swAppFileNewNotify** | 2 = Obsolete |
| **swAppFileNewNotify2** | 12 = [FileNewNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_FileNewNotify2EventHandler.html)  NOTE: Because it is possible to have a NULL active document when an add-in is notified using swAppFileOpenNotify2, use [ISldWorks::IGetOpenDocumentByName2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html) instead of [ISldWorks::IActiveDoc2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html). |
| **swAppFileNewPreNotify** | 26 = [FileNewPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_FileNewPreNotifyEventHandler.html) |
| **swAppFileOpenNotify** | 1 = Obsolete |
| **swAppFileOpenNotify2** | 13 = [FileOpenNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_FileOpenNotify2EventHandler.html) |
| **swAppFileOpenPostNotify** | 22 = [FileOpenPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_FileOpenPostNotifyEventHandler.html) |
| **swAppFileOpenPreNotify** | 21 = [FileOpenPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_FileOpenPreNotifyEventHandler.html) |
| **swAppInterfaceBrightnessThemeChangeNotify** | 35 = [InterfaceBrightnessThemeChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler.html) |
| **swAppJournalWriteNotify** | 27 = Not used. |
| **swAppLightPMCreateNotify** | Not used. |
| **swAppLightSheetCreateNotify** | 18 = [LightSheetCreateNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_LightSheetCreateNotifyEventHandler.html) |
| **swAppLightweightComponentOpenNotify** | 10 = Not used. |
| **swAppNonNativeFileOpenNotify** | 7 = [NonNativeFileOpenNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_NonNativeFileOpenNotifyEventHandler.html) |
| **swAppOn3DExperienceStateChangeNotify** | 46 = [On3DExperienceStateChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_On3DExperienceStateChangeNotifyEventHandler.html) |
| **swAppOnIdleNotify** | 20 = [OnIdleNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_OnIdleNotifyEventHandler.html) |
| **swAppPromptForFilenameNotify** | 15 = [PromptForFilenameNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_PromptForFilenameNotifyEventHandler.html) |
| **swAppPromptForMultipleFilenamesNotify** | 30 = [PromptForMultipleFileNamesNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_PromptForMultipleFileNamesNotifyEventHandler.html) |
| **swAppPropertySheetCreateNotify** | 6 = [PropertySheetCreateNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_PropertySheetCreateNotifyEventHandler.html) |
| **swAppReferencedFilePreNotify** | 23 = [ReferencedFilePreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_ReferencedFilePreNotifyEventHandler.html) |
| **swAppReferencedFilePreNotify2** | 36 = [ReferencedFilePreNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_ReferencedFilePreNotify2EventHandler.html) |
| **swAppReferenceNotFoundNotify** | 14 = [ReferenceNotFoundNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_ReferenceNotFoundNotifyEventHandler.html) |
| **swAppStandardsDatabaseChangeNotify** | 19 = Not used. |
| **swAppTaskPaneCollapseNotify** | 44 = [TaskPaneCollapseNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_TaskPaneCollapseNotifyEventHandler.html) |
| **swAppTaskPaneExpandNotify** | 43 = [TaskPaneExpandNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_TaskPaneExpandNotifyEventHandler.html) |
| **swAppTaskPaneHideNotify** | 41 = [TaskPaneHideNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_TaskPaneHideNotifyEventHandler.html) |
| **swAppTaskPanePinnedNotify** | 39 = [TaskPanePinnedNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_TaskPanePinnedNotifyEventHandler.html) |
| **swAppTaskPaneShowNotify** | 42 = [TaskPaneShowNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_TaskPaneShowNotifyEventHandler.html) |
| **swAppTaskPaneUnpinnedNotify** | 40 = [TaskPaneUnpinnedNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldworksEvents_TaskPaneUnpinnedNotifyEventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports SOLIDWORKS events ( <ATL\_object\_name>.h), include:

BEGIN\_SINK\_MAP(C<ATL\_object\_name>)

SINK\_ENTRY\_EX(ID\_SLDWORKS\_EVENTS, DIID\_DSldWorksEvents, swAppDocumentLoadNotify, DocumentLoadNotify)

SINK\_ENTRY\_EX(ID\_SLDWORKS\_EVENTS, DIID\_DSldWorksEvents, swAppFileNewNotify2, FileNewNotify2)

SINK\_ENTRY\_EX(ID\_SLDWORKS\_EVENTS, DIID\_DSldWorksEvents, swAppActiveDocChangeNotify, ActiveDocChangeNotify)

SINK\_ENTRY\_EX(ID\_SLDWORKS\_EVENTS, DIID\_DSldWorksEvents, swAppActiveModelDocChangeNotify, ActiveModelDocChangeNotify)

END\_SINK\_MAP()

If developing a C++ application, use the enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for the [ISldWorks](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swAppNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
