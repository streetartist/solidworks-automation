# IsModelOutOfDate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelOutOfDate`

Gets whether the model in this drawing view is up-to-date with the current model.
Gets whether the model in this drawing view is up-to-date with the current model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsModelOutOfDate() As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
value = instance.IsModelOutOfDate()
```

```

System.bool IsModelOutOfDate()
```

```

System.bool IsModelOutOfDate(); 
```

#### Return Value

True if the view is out of date, false if not

Remarks

A model can be out-of-date in a Detached drawing where the model is not loaded, if any of the views in any of the sheets in the drawing refers to a model that has been modified and saved to disk since this drawing was last saved. This situation is flagged upon opening a document as well.

If you are using [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) with the silent option enabled, this warning is returned via the Warnings argument by value swFileLoadWarning\_ModelOutOfDate. If you print this drawing and have the swRapidDraftPrintOutOfSynchWaterMark user preference enabled (see [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md)), then the printout will indicate this drawing as being out-of-synch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IsModelLoaded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelLoaded.md)  
[IView::LoadModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~LoadModel.md)
