# INote Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members`

Allows you to get standard note information.
The following tables list the members exposed by [INote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [AllUpperCase](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AllUpperCase.md) | Gets or sets whether the text of this note is all uppercase. |
| Property | [Angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~Angle.md) | Controls the rotation angle of this note. |
| Property | [BehindSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BehindSheet.md) | Places this note, located on the sheet format in a drawing, behind the drawing sheet. |
| Property | [HasMultipleFonts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts.md) | Gets whether a note contains multiple fonts. |
| Property | [IncludeDimPrefixSuffixTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IncludeDimPrefixSuffixTolerance.md) | Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note. |
| Property | [IsBendLineNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBendLineNote.md) | Gets whether this note is a bendline note. |
| Property | [LockPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.md) | Gets and sets whether to anchor this note. |
| Property | [PromptText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PromptText.md) | Gets and sets the message prompt text. |
| Property | [PropertyLinkedText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.md) | Gets or sets the text for the note using the values of the properties linked to the note. |
| Property | [ReadOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ReadOnly.md) | Gets or sets the read-only state of a note. |
| Property | [TagName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TagName.md) | Gets or sets the tag name for this note. |
| Property | [TextRightToLeft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TextRightToLeft.md) | Gets or sets whether notes are displayed right to left. |
| Property | [ToBoundingBox](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ToBoundingBox.md) | Gets and sets whether to select the **To bounding box** option for leaders in this note's PropertyManager page. |
| Property | [Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~Visible.md) | Gets and sets the visibility state of a note during the creation of a block. |
| Property | [WatermarkBehindGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry.md) | Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or assembly. |
| Property | [WatermarkNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.md) | Gets or sets whether the note is a watermark in a part or assembly. |
| Property | [WatermarkTransparencyLevel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.md) | Gets or sets the transparency level of a note specified to be a watermark. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Adds text to the selected compound note. |
| Method | [BeginSketchEdit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BeginSketchEdit.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Activates the sketch of the compound note. |
| Method | [EndSketchEdit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~EndSketchEdit.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Finishes accessing this compound note's sketch. |
| Method | [GetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAnnotation.md) | Gets the annotation for this specific note. |
| Method | [GetArcAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArcAtIndex.md) | Gets information for the specified arc in this note. |
| Method | [GetArcCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArcCount.md) | Gets the number of arcs in the note. |
| Method | [GetArrowHeadAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadAtIndex.md) | Gets information on the specified arrowhead in this note. |
| Method | [GetArrowHeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadCount.md) | Gets the number of arrowheads in the note. |
| Method | [GetArrowHeadInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArrowHeadInfo.md) | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | [GetAttachPos](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetAttachPos.md) | Gets the attachment point of this note. |
| Method | [GetBalloonInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonInfo.md) | Gets information describing the geometry of the balloon, if any, that encloses the note text. |
| Method | [GetBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.md) | Gets the balloon options for this note. |
| Method | [GetBalloonPadding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonPadding.md) | Gets the balloon padding of this note. |
| Method | [GetBalloonSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonSize.md) | Gets the balloon size or fit of this note. |
| Method | [GetBalloonStack](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStack.md) | Gets the balloon stack for this balloon note. |
| Method | [GetBalloonStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonStyle.md) | Gets the balloon style of this note. |
| Method | [GetBendLineValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues.md) | Obsolete. Superseded by [INote::GetBendLineValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues2.md). |
| Method | [GetBendLineValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues2.md) | Gets the values of a bend line note. |
| Method | [GetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.md) | Gets the text for this BOM balloon note. |
| Method | [GetBomBalloonTextStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonTextStyle.md) | Gets the text style of this BOM balloon note. |
| Method | [GetCompoundTextAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the text item corresponding to the specified index from a compound note. |
| Method | [GetCompoundTextCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextCount.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the number of text items in a compound note. |
| Method | [GetExtent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtent.md) | Gets the extents of a note in sheet space. |
| Method | [GetExtentAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtentAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the extents of the specified piece of text within a compound note. |
| Method | [GetFontInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetFontInfo.md) | Gets with the note's font information. |
| Method | [GetHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeight.md) | Get the note's height. |
| Method | [GetHeightAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the specified text item's height in a compound note. |
| Method | [GetHeightInPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightInPoints.md) | Gets the height of this note in points (for example, 8, 10, 12, and so on). |
| Method | [GetHyperlinkText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHyperlinkText.md) | Gets the hyperlink in a note. |
| Method | [GetLeaderAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderAtIndex.md) | Gets information about the specified leader on this note. |
| Method | [GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderCount.md) | Gets the number of leaders on this note. |
| Method | [GetLeaderInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderInfo.md) | Gets information describing the layout of the note leader lines. |
| Method | [GetLeaderNumPointsAt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLeaderNumPointsAt.md) | Gets the number of points in the specified leader of this note. |
| Method | [GetLineAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineAtIndex.md) | Gets information for the specified line. |
| Method | [GetLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineCount.md) | Gets the number of line segments in this note. |
| Method | [GetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetName.md) | Gets the name of this note. |
| Method | [GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetNext.md) | Gets the next note in [drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md). |
| Method | [GetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetSketch.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the sketch for the current compound note. |
| Method | [GetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetText.md) | Gets this note's text. |
| Method | [GetTextAngleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAngleAtIndex.md) | Gets the text angle for the specified piece of text in this note. |
| Method | [GetTextAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAtIndex.md) | Gets the specified text in this note. |
| Method | [GetTextCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextCount.md) | Gets the number of text items in this note. |
| Method | [GetTextFontAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.md) | Gets the font used by the specified text item in this note. |
| Method | [GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFormat.md) | Obsolete. Superseded by [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md) and [IAnnotation::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md). |
| Method | [GetTextFormatAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFormatAtIndex.md) | Obsolete. Superseded by [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md) and [IAnnotation::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md). |
| Method | [GetTextHeightAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextHeightAtIndex.md) | Gets the text height for the specified piece of text in this note. |
| Method | [GetTextInvertAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextInvertAtIndex.md) | Gets the specified text item's invert flag. |
| Method | [GetTextJustification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustification.md) | Gets the text justification of a standard note. |
| Method | [GetTextJustificationAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the text justification for the specified text item in a compound note. |
| Method | [GetTextLineSpacingAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextLineSpacingAtIndex.md) | Gets the line spacing for this note. |
| Method | [GetTextOffsetAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the text item's offset relative to note's text point in a compound note. |
| Method | [GetTextPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPoint.md) | Obsolete. Superseded by [INote::GetTextPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPoint2.md) or [INote::IGetTextPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPoint2.md). |
| Method | [GetTextPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPoint2.md) | Gets the note's text reference point (i.e., note origin). |
| Method | [GetTextPositionAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPositionAtIndex.md) | Gets the text item's offset relative to the document origin. |
| Method | [GetTextRefPositionAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextRefPositionAtIndex.md) | Gets the specified text item's reference position in this note; for example, the upper left, lower left, or center. |
| Method | [GetTextVerticalJustification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextVerticalJustification.md) | Gets the vertical justification of a standard note. |
| Method | [GetTriangleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTriangleAtIndex.md) | Gets the triangle at the specified index. |
| Method | [GetTriangleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTriangleCount.md) | Gets the number of triangles in this note. |
| Method | [GetUpperRight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetUpperRight.md) | Gets the note's upper-right text point. |
| Method | [GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetUseDocTextFormat.md) | Obsolete. Superseded by [IAnnotation::GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.md). |
| Method | [HasBalloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasBalloon.md) | Gets whether this note has a balloon. |
| Method | [HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasExtraLeader.md) | Gets whether this note has a bent or straight leaderline. |
| Method | [IGetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAnnotation.md) | Gets the annotation for this specific note. |
| Method | [IGetArcAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArcAtIndex.md) | Gets information for the specified arc in this note. |
| Method | [IGetArrowHeadAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadAtIndex.md) | Gets information on the specified arrowhead in this note. |
| Method | [IGetArrowHeadInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArrowHeadInfo.md) | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | [IGetAttachPos](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetAttachPos.md) | Gets the attachment point of this note. |
| Method | [IGetBalloonInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetBalloonInfo.md) | Gets information describing the geometry of the balloon, if any, that encloses the note text. |
| Method | [IGetExtent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtent.md) | Gets the extents of a note in sheet space. |
| Method | [IGetExtentAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtentAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the extents of the specified piece of text within a compound note. |
| Method | [IGetFontInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetFontInfo.md) | Gets with the note's font information. |
| Method | [IGetLeaderAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderAtIndex.md) | Gets information about the specified leader on this note. |
| Method | [IGetLeaderInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLeaderInfo.md) | Gets information describing the layout of the note leader lines. |
| Method | [IGetLineAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLineAtIndex.md) | Gets information for the specified line. |
| Method | [IGetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetNext.md) | Gets the next note in [drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md). |
| Method | [IGetSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetSketch.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the sketch for the current compound note. |
| Method | [IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextFormat.md) | Obsolete. Superseded by [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md) and [IAnnotation::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md). |
| Method | [IGetTextFormatAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextFormatAtIndex.md) | Obsolete. Superseded by [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md) and [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md). |
| Method | [IGetTextOffsetAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextOffsetAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets whether the text item's offset relative to note's text point in a compound note. |
| Method | [IGetTextPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPoint.md) | Obsolete. Superseded by [INote::IGetTextPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPoint2.md). |
| Method | [IGetTextPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPoint2.md) | Gets the note's text reference point (i.e., note origin). |
| Method | [IGetTextPositionAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextPositionAtIndex.md) | Gets the text item's offset relative to the document origin. |
| Method | [IGetTriangleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTriangleAtIndex.md) | Gets the triangle at the specified index. |
| Method | [IGetUpperRight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetUpperRight.md) | Gets the note's upper-right text point. |
| Method | [IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttached.md) | Gets whether the note is attached. |
| Method | [IsAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsAttribute.md) | Obsolete. Not superseded. |
| Method | [IsBomBalloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBomBalloon.md) | Gets whether this note has a BOM balloon. |
| Method | [IsCompoundNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Gets whether the current note is a compound note. |
| Method | [ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ISetTextFormat.md) | Obsolete. Superseded by [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) and [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md). |
| Method | [ISetTextFormatAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ISetTextFormatAtIndex.md) | Obsolete. Superseded by [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) and [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md). |
| Method | [IsStackedBalloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.md) | Gets whether this note is part of a stacked balloon. |
| Method | [IsStackedBalloonMaster](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloonMaster.md) | Gets whether this note is the master note of a balloon stack. |
| Method | [MakeStackedBalloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.md) | Converts this balloon to a stacked balloon. |
| Method | [SetBalloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloon.md) | Sets the balloon style, size, and fit for this note. |
| Method | [SetBalloonPadding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBalloonPadding.md) | Sets the padding for this balloon note. |
| Method | [SetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.md) | Sets the text for this BOM balloon note. |
| Method | [SetHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeight.md) | Sets the height of this note in meters. |
| Method | [SetHeightInPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeightInPoints.md) | Sets the height of this note in points (for example, 8, 10, 12, and so on). |
| Method | [SetHyperlinkText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHyperlinkText.md) | Sets the hyperlink in a note. |
| Method | [SetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetName.md) | Sets the name for this note. |
| Method | [SetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetText.md) | Sets the text of the note. |
| Method | [SetTextAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Sets the text value at the specified index within the compound note. |
| Method | [SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextFormat.md) | Obsolete. Superseded by [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) and [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md). |
| Method | [SetTextFormatAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextFormatAtIndex.md) | Obsolete. Superseded by [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) and [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md). |
| Method | [SetTextJustification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustification.md) | Sets the text justification of a standard note. |
| Method | [SetTextJustificationAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Sets the text justification for the specified text item in a compound note. |
| Method | [SetTextOffsetAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Relocates the offset (origin) of the specified piece of text in a compound note. |
| Method | [SetTextPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.md) | Relocates the note origin to the specified location. |
| Method | [SetTextVerticalJustification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextVerticalJustification.md) | Sets the vertical justification of a standard note. |
| Method | [SetZeroLengthLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.md) | Obsolete for documents created in SOLIDWORKS 2016 and later. Sets a 0-length leader for a compound note. |

[Top](#top)

 

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDoc2::InsertNewNote3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertNewNote3.md)  
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)
