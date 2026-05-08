# swDrawingNotify_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDrawingNotify_e`

Drawing notifications.
Drawing notifications.

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

<System.Runtime.InteropServices.GuidAttribute("1DE96FE3-4131-4622-996E-9C387023CAD0")>
Public Enum swDrawingNotify_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swDrawingNotify_e
```

```

[System.Runtime.InteropServices.Guid("1DE96FE3-4131-4622-996E-9C387023CAD0")]
public enum swDrawingNotify_e : System.Enum 
```

```

public enum swDrawingNotify_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("1DE96FE3-4131-4622-996E-9C387023CAD0")
public enum swDrawingNotify_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("1DE96FE3-4131-4622-996E-9C387023CAD0")]
__value public enum swDrawingNotify_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("1DE96FE3-4131-4622-996E-9C387023CAD0")]
public enum class swDrawingNotify_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swDrawingActivateSheetPostNotify** | 53 = [ActivateSheetPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ActivateSheetPostNotifyEventHandler.html) |
| **swDrawingActivateSheetPreNotify** | 52 = [ActivateSheetPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ActivateSheetPreNotifyEventHandler.html) |
| **swDrawingAddCustomPropertyNotify** | 20 = [AddCustomPropertyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_AddCustomPropertyNotifyEventHandler.html) |
| **swDrawingAddDvePagePreNotify** | 40 = Not used. |
| **swDrawingAddItemNotify** | 15 = [AddItemNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_AddItemNotifyEventHandler.html) |
| **swDrawingAutoSaveNotify** | 10 = [AutoSaveNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_AutoSaveNotifyEventHandler.html) |
| **swDrawingAutoSaveToStorageNotify** | 11 = [AutoSaveToStorageNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_AutoSaveToStorageNotifyEventHandler.html) |
| **swDrawingAutoSaveToStorageStoreNotify** | 48 = [AutoSaveToStorageStoreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_AutoSaveToStorageStoreNotifyEventHandler.html) |
| **swDrawingChangeCustomPropertyNotify** | 21 = [ChangeCustomPropertyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ChangeCustomPropertyNotifyEventHandler.html) |
| **swDrawingClearSelectionsNotify** | 37 = [ClearSelectionsNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ClearSelectionsNotifyEventHandler.html) |
| **swDrawingCommandManagerTabActivatedPreNotify** | 54 = [CommandManagerTabActivatedPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler.html) |
| **swDrawingConfigChangeNotify** | 12 = [ActiveConfigChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ActiveConfigChangeNotifyEventHandler.html) |
| **swDrawingConfigChangePostNotify** | 13 = [ActiveConfigChangePostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ActiveConfigChangePostNotifyEventHandler.html) |
| **swDrawingDeleteCustomPropertyNotify** | 22 = [DeleteCustomPropertyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DeleteCustomPropertyNotifyEventHandler.html) |
| **swDrawingDeleteItemNotify** | 17 = [DeleteItemNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DeleteItemNotifyEventHandler.html) |
| **swDrawingDeleteItemPreNotify** | 36 = [DeleteItemPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DeleteItemPreNotifyEventHandler.html) |
| **swDrawingDeleteSelectionPreNotify** | 24 = [DeleteSelectonPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DeleteSelectionPreNotifyEventHandler.html) |
| **swDrawingDestroyNotify** | 2 = Obsolete |
| **swDrawingDestroyNotify2** | 42 = [DestroyNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DestroyNotify2EventHandler.html) |
| **swDrawingDimensionChangeNotify** | 32 = [DimensionChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DimensionChangeNotifyEventHandler.html) |
| **swDrawingDisplayPaneCollapseNotify** | 59 = [DisplayPaneCollapseNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DisplayPaneCollapseNotifyEventHandler.html) |
| **swDrawingDisplayPaneExpandNotify** | 58 = [DisplayPaneExpandNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DisplayPaneExpandNotifyEventHandler.html) |
| **swDrawingDynamicHighlightNotify** | 31 = [DynamicHighlightNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DynamicHighlightNotifyEventHandler.html) |
| **swDrawingEquationEditorPostNotify** | 39 = [EquationEditorPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_EquationEditorPostNotifyEventHandler.html) |
| **swDrawingEquationEditorPreNotify** | 38 = [EquationEditorPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_EquationEditorPreNotifyEventHandler.html) |
| **swDrawingFeatureManagerTabActivatedNotify** | 56 = [FeatureManagerTabActivatedNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedNotifyEventHandler.html) |
| **swDrawingFeatureManagerTabActivatedPreNotify** | 55 = [FeatureManagerTabActivatedPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.html) |
| **swDrawingFeatureManagerTreeRebuildNotify** | 29 = [FeatureManagerTreeRebuildNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.html) |
| **swDrawingFileReloadCancelNotify** | 33 = Not used. |
| **swDrawingFileReloadNotify** | 19 = Not used. |
| **swDrawingFileReloadPreNotify** | 25 = Not used. |
| **swDrawingFileSaveAsNotify** | 7 = Obsolete |
| **swDrawingFileSaveAsNotify2** | 23 = [FileSaveAsNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.html) |
| **swDrawingFileSaveNotify** | 6 = [FileSaveNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSaveNotifyEventHandler.html) |
| **swDrawingFileSavePostCancelNotify** | 34 = [FileSavePostCancelNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSavePostCancelNotifyEventHandler.html) |
| **swDrawingFileSavePostNotify** | 26 = [FileSavePostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_FileSavePostNotifyEventHandler.html) |
| **swDrawingInsertTableNotify** | 49 = [InsertTableNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_InsertTableNotifyEventHandler.html) |
| **swDrawingLoadFromStorageNotify** | 8 = [LoadFromStorageNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_LoadFromStorageNotifyEventHandler.html) |
| **swDrawingLoadFromStorageStoreNotify** | 27 = [LoadFromStorageStoreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_LoadFromStorageStoreNotifyEventHandler.html) |
| **swDrawingModifyNotify** | 18 = [ModifyNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ModifyNotifyEventHandler.html) |
| **swDrawingModifyTableNotify** | 50 = [ModifyTableNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ModifyTableNotifyEventHandler.html) |
| **swDrawingNewSelectionNotify** | 5 = [NewSelectionNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_NewSelectionNotifyEventHandler.html) |
| **swDrawingRedoPostNotify** | 45 = [RedoPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_RedoPostNotifyEventHandler.html) |
| **swDrawingRedoPreNotify** | 46 = [RedoPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_RedoPreNotifyEventHandler.html) |
| **swDrawingRegenNotify** | 1 = [RegenNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_RegenNotifyEventHandler.html) |
| **swDrawingRegenPostNotify** | 3 = [RegenPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_RegenPostNotifyEventHandler.html) |
| **swDrawingRenameDisplayTitleNotify** | 57 = [RenameDisplayTitleNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler.html) |
| **swDrawingRenameItemNotify** | 16 = [RenameItemNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_RenameItemNotifyEventHandler.html) |
| **swDrawingSaveToStorageNotify** | 9 = [SaveToStorageNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_SaveToStorageNotifyEventHandler.html) |
| **swDrawingSaveToStorageStoreNotify** | 28 = [SaveToStorageStoreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_SaveToStorageStoreNotifyEventHandler.html) |
| **swDrawingSketchSolveNotify** | 35 = [SketchSolveNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_SketchSolveNotifyEventHandler.html) |
| **swDrawingStateChangeNotify** | 60 = [DrawingStateChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_DrawingStateChangeNotifyEventHandler.html) |
| **swDrawingUndoPostNotify** | 43 = [UndoPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_UndoPostNotifyEventHandler.html) |
| **swDrawingUndoPreNotify** | 47 = [UndoPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_UndoPreNotifyEventHandler.html) |
| **swDrawingUnitsChangeNotify** | 41 = [UnitsChangeNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_UnitsChangeNotifyEventHandler.html) |
| **swDrawingUserSelectionPostNotify** | 51 = [UserSelectionPostNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_UserSelectionPostNotifyEventHandler.html) |
| **swDrawingUserSelectionPreNotify** | 44 = [UserSelectionPreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_UserSelectionPreNotifyEventHandler.html) |
| **swDrawingViewCreatePreNotify** | 30 = [ViewCreatePreNotify](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingDocEvents_ViewCreatePreNotifyEventHandler.html) |
| **swDrawingViewNewNotify** | 4 = Obsolete |
| **swDrawingViewNewNotify2** | 14 = [ViewNewNotify2](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DDrawingdocevents_ViewNewNotify2EventHandler.html) |

Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports drawing events (e.g., Drawing.h), include:

BEGIN\_SINK\_MAP(CSwDrawing)

SINK\_ENTRY\_EX(ID\_DRAWINGDOC\_EVENTS, DIID\_DDrawingDocEvents, swDrawingDestroyNotify, DestroyNotify)

SINK\_ENTRY\_EX(ID\_DRAWINGDOC\_EVENTS, DIID\_DDrawingDocEvents, swDrawingNewSelectionNotify, NewSelectionNotify)

END\_SINK\_MAP()

If developing a C++ application, use the enumerators to [register for notifications](sldworksapiprogguide.chm::/overview/events.htm) for [IDrawingDoc](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html) events.

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swDrawingNotify\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
