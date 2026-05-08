# AutoBalloon4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon4`

Obsolete. Superseded by IDrawingDoc::AutoBalloon5.
Obsolete. Superseded by [IDrawingDoc::AutoBalloon5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AutoBalloon4( _
   ByVal Layout As System.Integer, _
   ByVal IgnoreMultiple As System.Boolean, _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextContent As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextContent As System.Integer, _
   ByVal LowerText As System.String, _
   ByVal Layername As System.String, _
   ByVal BalloonsToFaces As System.Boolean _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim Layout As System.Integer
Dim IgnoreMultiple As System.Boolean
Dim Style As System.Integer
Dim Size As System.Integer
Dim UpperTextContent As System.Integer
Dim UpperText As System.String
Dim LowerTextContent As System.Integer
Dim LowerText As System.String
Dim Layername As System.String
Dim BalloonsToFaces As System.Boolean
Dim value As System.Object
 
value = instance.AutoBalloon4(Layout, IgnoreMultiple, Style, Size, UpperTextContent, UpperText, LowerTextContent, LowerText, Layername, BalloonsToFaces)
```

```

System.object AutoBalloon4( 
   System.int Layout,
   System.bool IgnoreMultiple,
   System.int Style,
   System.int Size,
   System.int UpperTextContent,
   System.string UpperText,
   System.int LowerTextContent,
   System.string LowerText,
   System.string Layername,
   System.bool BalloonsToFaces
)
```

```

System.Object^ AutoBalloon4( 
   System.int Layout,
   System.bool IgnoreMultiple,
   System.int Style,
   System.int Size,
   System.int UpperTextContent,
   System.String^ UpperText,
   System.int LowerTextContent,
   System.String^ LowerText,
   System.String^ Layername,
   System.bool BalloonsToFaces
) 
```

#### Parameters

*Layout*
:   Layout style of the balloons as defined by [swBalloonLayoutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonLayoutType_e.html) or specify -1 for this argument to use the document default layout style

*IgnoreMultiple*
:   True to apply a balloon to only one instance of a component, false to apply balloons to all instances of that component

*Style*
:   Style of the balloons as defined by [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html) or specify -1 to use the document default balloon style

*Size*
:   Fit of balloon as defined by [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html) or specify -1 to use the document default balloon fit

*UpperTextContent*
:   Upper-text content style as defined by [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html) or specify -1 to use the document default upper text content

*UpperText*
:   Text for upper balloon

*LowerTextContent*
:   Lower-text content style as defined by [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html) or specify -1 to use the document default lower text content

    **NOTE:** This and the next argument are only effective when Style is set to swBS\_SplitCirc. See the SOLIDWORKS Help for additional details about autoballoons.

*LowerText*
:   Text for lower balloon

*Layername*
:   Name of the layer for this balloon

*BalloonsToFaces*
:   True to attach balloons to faces; false to attach balloons to edges

#### Return Value

Array of newly created [notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)

Remarks

This method automatically creates the BOM balloons for the selected drawing views. If a drawing sheet is selected, BOM balloons are automatically created for all of the drawing views on that drawing sheet.

|  |  |
| --- | --- |
| To get or set default values for... | Use... |
| Layout | [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md)(swUserPreferenceIntegerValue\_e.swDetailingAutoBalloonLayout, swUserPreferenceOption\_e.swDetailingNoOptionSpecified)   - or -  [IModelDocExtension::SetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md)(swUserPreferenceIntegerValue\_e.swDetailingAutoBalloonLayout, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonLayoutType\_e.<Value>) |
| Style | IModelDocExtension::GetUserPreferenceInteger((swUserPreferenceIntegerValue\_e.swDetailingBOMBalloonStyle, swUserPreferenceOption\_e.swDetailingNoOptionSpecified)  - or -  IModelDocExtension::SetUserPreferenceInteger(swUserPreferenceIntegerValue\_e.swDetailingBOMBalloonFit, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonFit\_e.<Value>) |
| Size | IModelDocExtension::GetUserPreferenceInteger((swUserPreferenceIntegerValue\_e.swDetailingBOMBalloonFit, swUserPreferenceOption\_e.swDetailingNoOptionSpecified)  - or -  (swUserPreferenceIntegerValue\_e.swDetailingBOMStackedBalloonFit, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonFit\_e.<Value>) |
| UpperTextContent | IModelDocExtension::GetUserPreferenceInteger(swUserPreferenceIntegerValue\_e.swDetailingBOMUpperText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified)  -  or -  IModelDocExtension::SetUserPreferenceInteger(swUserPreferenceIntegerValue\_e.swDetailingBOMUpperText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonTextContent\_e.<Value>) |
| LowerTextContent | IModelDocExtension::GetUserPreferenceInteger(swUserPreferenceIntegerValue\_e.swDetailingBOMLowerText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified)  - or -  IModelDocExtension::SetUserPreferenceInteger(swUserPreferenceIntegerValue\_e.swDetailingBOMLowerText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonTextContent\_e.<Value>) |

This method also allows you to get only the balloons just created.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IModelDocExtension::InsertBOMBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon.md)
