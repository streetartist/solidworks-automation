# swPartNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPartNotify_e`

Part notifications.
Part notifications.

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

<System.Runtime.InteropServices.GuidAttribute("D767038A-05F6-43F3-A863-0989E8368ACC")>
Public Enum swPartNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swPartNotify_e
```

```

[System.Runtime.InteropServices.Guid("D767038A-05F6-43F3-A863-0989E8368ACC")]
public enum swPartNotify_e : System.Enum 
```

```

public enum swPartNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D767038A-05F6-43F3-A863-0989E8368ACC")
public enum swPartNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D767038A-05F6-43F3-A863-0989E8368ACC")]
__value public enum swPartNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D767038A-05F6-43F3-A863-0989E8368ACC")]
public enum class swPartNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swPartActiveAnnotationViewChangeNotify** | 80 = [ActiveAnnotationViewChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveAnnotationViewChangeNotifyEventHandler.html) |
| **swPartActiveDisplayStateChangePostNotify** | 61 = [ActiveDisplayStateChangePostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.html) |
| **swPartActiveDisplayStateChangePreNotify** | 60 = [ActiveDisplayStateChangePreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.html) |
| **swPartActiveViewChangeNotify** | 53 = [ActiveViewChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveViewChangeNotifyEventHandler.html) |
| **swPartAddCustomPropertyNotify** | 21 = [AddCustomPropertyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_AddCustomPropertyNotifyEventHandler.html) |
| **swPartAddDvePagePreNotify** | Not used |
| **swPartAddItemNotify** | 16 = [AddItemNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_AddItemNotifyEventHandler.html) |
| **swPartAutoSaveNotify** | 12 = [AutoSaveNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_AutoSaveNotifyEventHandler.html) |
| **swPartAutoSaveToStorageNotify** | 13 = [AutoSaveToStorageNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_AutoSaveToStorageNotifyEventHandler.html) |
| **swPartAutoSaveToStorageStoreNotify** | 66 = [AutoSaveToStorageStoreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_AutoSaveToStorageStoreNotifyEventHandler.html) |
| **swPartBodyVisibleChangeNotify** | 29 = [BodyVisibleChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_BodyVisibleChangeNotifyEventHandler.html) |
| **swPartChangeCustomPropertyNotify** | 22 = [ChangeCustomPropertyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ChangeCustomPropertyNotifyEventHandler.html) |
| **swPartClearSelectionsNotify** | 42 = [ClearSelectionsNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ClearSelectionsNotifyEventHandler.html) |
| **swPartCloseDesignTableNotify** | 46 = [CloseDesignTableNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_CloseDesignTableNotifyEventHandler.html) |
| **swPartCommandManagerTabActivatedPreNotify** | 71 = [CommandManagerTabActivatedPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_CommandManagerTabActivatedPreNotifyEventHandler.html) |
| **swPartConfigChangeNotify** | 10 = [ActiveConfigChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveConfigChangeNotifyEventHandler.html) |
| **swPartConfigChangePostNotify** | 11 = [ActiveConfigChangePostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveConfigChangePostNotifyEventHandler.html) |
| **swPartConfigurationChangeNotify** | 51 = [ConfigurationChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ConfigurationChangeNotifyEventHandler.html) |
| **swPartConvertToBodiesPostNotify** | 78 = [ConvertToBodiesPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ConvertToBodiesPostNotifyEventHandler.html) |
| **swPartConvertToBodiesPreNotify** | 77 = [ConvertToBodiesPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ConvertToBodiesPreNotifyEventHandler.html) |
| **swPartDeleteCustomPropertyNotify** | 23 = [DeleteCustomPropertyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DeleteCustomPropertyNotifyEventHandler.html) |
| **swPartDeleteItemNotify** | 18 = [DeleteItemNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DeleteItemNotifyEventHandler.html) |
| **swPartDeleteItemPreNotify** | 41 = [DeleteItemPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DeleteItemPreNotifyEventHandler.html) |
| **swPartDeleteSelectionPreNotify** | 27 = [DeleteSelectionPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DeleteSelectionPreNotifyEventHandler.html) |
| **swPartDestroyNotify** | Obsolete |
| **swPartDestroyNotify2** | 50 = [DestroyNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DestroyNotify2EventHandler.html) |
| **swPartDimensionChangeNotify** | 37 = [DimensionChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DimensionChangeNotifyEventHandler.html) |
| **swPartDisplayPaneCollapseNotify** | 82 = [DisplayPaneCollapseNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DisplayPaneCollapseNotifyEventHandler.html) |
| **swPartDisplayPaneExpandNotify** | 81 = [DisplayPaneExpandNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DisplayPaneExpandNotifyEventHandler.html) |
| **swPartDragStateChangeNotify** | 67 = [DragStateChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DragStateChangeNotifyEventHandler.html) |
| **swPartDynamicHighlightNotify** | 36 = [DynamicHighlightNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_DynamicHighlightNotifyEventHandler.html) |
| **swPartEquationEditorPostNotify** | 44 = [EquationEditorPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_EquationEditorPostNotifyEventHandler.html) |
| **swPartEquationEditorPreNotify** | 43 = [EquationEditorPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_EquationEditorPreNotifyEventHandler.html) |
| **swPartFeatureEditPreNotify** | 24 = [FeatureEditPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FeatureEditPreNotifyEventHandler.html) |
| **swPartFeatureManagerFilterStringChangeNotify** | 54 = [FeatureManagerFilterStringChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FeatureManagerFilterStringChangeNotifyEventHandler.html) |
| **swPartFeatureManagerTabActivatedNotify** | 75 = [FeatureManagerTabActivatedNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler.html) |
| **swPartFeatureManagerTabActivatedPreNotify** | 74 = [FeatureManagerTabActivatedPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.html) |
| **swPartFeatureManagerTreeRebuildNotify** | 34 = [FeatureManagerTreeRebuildNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.html) |
| **swPartFeatureSketchEditPreNotify** | 25 = [FeatureSketchEditPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FeatureSketchEditPreNotifyEventHandler.html) |
| **swPartFileDropPostNotify** | 35 = [FileDropPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileDropPostNotifyEventHandler.html) |
| **swPartFileDropPreNotify** | 56 = [FileDropPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileDropPreNotifyEventHandler.html) |
| **swPartFileReloadCancelNotify** | 38 = [FileReloadCancelNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileReloadCancelNotifyEventHandler.html) |
| **swPartFileReloadNotify** | 20 = [FileReloadNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileReloadNotifyEventHandler.html) |
| **swPartFileReloadPreNotify** | 28 = [FileReloadPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileReloadPreNotifyEventHandler.html) |
| **swPartFileSaveAsNotify** | Obsolete |
| **swPartFileSaveAsNotify2** | 26 = [FileSaveAsNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler.html) |
| **swPartFileSaveNotify** | 6 = [FileSaveNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSaveNotifyEventHandler.html) |
| **swPartFileSavePostCancelNotify** | 39 = [FileSavePostCancelNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSavePostCancelNotifyEventHandler.html) |
| **swPartFileSavePostNotify** | 31 = [FileSavePostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FileSavePostNotifyEventHandler.html) |
| **swPartFlipLoopNotify** | 55 = [FlipLoopNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_FlipLoopNotifyEventHandler.html) |
| **swPartInsertTableNotify** | 68 = [InsertTableNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_InsertTableNotifyEventHandler.html) |
| **swPartLightingDialogCreateNotify** | 15 = [LightingDialogCreateNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_LightingDialogCreateNotifyEventHandler.html) |
| **swPartLoadFromStorageNotify** | 8 = [LoadFromStorageNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_LoadFromStorageNotifyEventHandler.html) |
| **swPartLoadFromStorageStoreNotify** | 32 = [LoadFromStorageStoreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_LoadFromStorageStoreNotifyEventHandler.html) |
| **swPartModifyNotify** | 19 = [ModifyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ModifyNotifyEventHandler.html) |
| **swPartModifyTableNotify** | 69 = [ModifyTableNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ModifyTableNotifyEventHandler.html) |
| **swPartNewSelectionNotify** | 5 = [NewSelectionNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_NewSelectionNotifyEventHandler.html) |
| **swPartOpenDesignTableNotify** | 45 = [OpenDesignTableNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_OpenDesignTableNotifyEventHandler.html) |
| **swPartPreRenameItemNotify** | 72 = [PreRenameItemNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PreRenameItemNotifyEventHandler.html) |
| **swPartPromptBodiesToKeepNotify** | 47 = [PromptBodiesToKeepNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_PromptBodiesToKeepNotifyEventHandler.html) |
| **swPartPublishTo3DPDFNotify** | 78 = [PublishTo3DPDFNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_PublishTo3DPDFNotifyEventHandler.html) |
| **swPartRedoPostNotify** | 62 = [RedoPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_RedoPostNotifyEventHandler.html) |
| **swPartRedoPreNotify** | 63 = [RedoPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_RedoPreNotifyEventHandler.html) |
| **swPartRegenNotify** | 1 = [RegenNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_RegenNotifyEventHandler.html) |
| **swPartRegenPostNotify** | Obsolete |
| **swPartRegenPostNotify2** | 30 = [RegenPostNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_RegenPostNotify2EventHandler.html) |
| **swPartRenamedDocumentNotify** | 73 = [RenamedDocumentNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenamedDocumentNotifyEventHandler.html) |
| **swPartRenameDisplayTitleNotify** | 79 = [RenameDisplayTitleNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenameDisplayTitleNotifyEventHandler.html) |
| **swPartRenameItemNotify** | 17 = [RenameItemNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_RenameItemNotifyEventHandler.html) |
| **swPartSaveToStorageNotify** | 9 = [SaveToStorageNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_SaveToStorageNotifyEventHandler.html) |
| **swPartSaveToStorageStoreNotify** | 33 = [SaveToStorageStoreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_SaveToStorageStoreNotifyEventHandler.html) |
| **swPartSensorAlertPreNotify** | 57 = [SensorAlertPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.html) |
| **swPartSketchSolveNotify** | 40 = [SketchSolveNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_SketchSolveNotifyEventHandler.html) |
| **swPartSuppressionStateChangeNotify** | 52 = [SuppressionStateChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_SuppressionStateChangeNotifyEventHandler.html) |
| **swPartUndoPostNotify** | 58 = [UndoPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_UndoPostNotifyEventHandler.html) |
| **swPartUndoPreNotify** | 64 = [UndoPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_UndoPreNotifyEventHandler.html) |
| **swPartUnitsChangeNotify** | 49 = [UnitsChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_UnitsChangeNotifyEventHandler.html) |
| **swPartUserSelectionPostNotify** | 70 = [UserSelectionPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_UserSelectionPostNotifyEventHandler.html) |
| **swPartUserSelectionPreNotify** | 59 = [UserSelectionPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.html) |
| **swPartViewNewNotify** | Obsolete |
| **swPartViewNewNotify2** | 14 = [ViewNewNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ViewNewNotify2EventHandler.html) |
| **swPartWeldmentCutListUpdatePostNotify** | 65 = [WeldmentCutListUpdatePostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object. For example:

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports part events (e.g., PartDoc.h), include:

BEGIN\_SINK\_MAP(CSwPart)

SINK\_ENTRY\_EX(ID\_PARTDOC\_EVENTS, DIID\_DPartDocEvents, swPartDestroyNotify, DestroyNotify)

SINK\_ENTRY\_EX(ID\_PARTDOC\_EVENTS, DIID\_DPartDocEvents, swPartNewSelectionNotify, NewSelectionNotify)

END\_SINK\_MAP()

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for [IPartDoc](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swPartNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
