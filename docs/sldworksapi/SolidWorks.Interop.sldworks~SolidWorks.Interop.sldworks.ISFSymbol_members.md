# ISFSymbol Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members`

Allows access to display information for surface finish symbols.
The following tables list the members exposed by [ISFSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [GOSTDefaultSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GOSTDefaultSymbol.md) | Gets whether the GOST Add default symbol option is set. |
| Property | [GOSTNotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GOSTNotation.md) | Gets whether the GOST Use for notation option is set. |
| Property | [Grinding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Grinding.md) | Obsolete. Superseded by [ISFSymbol::GetSymbolSurfaceTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolSurfaceTexture.md). |
| Property | [Orientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Orientation.md) | Gets whether the orientation of this surface finish symbol is relative to the model or entity to which it is attached. |
| Property | [ProfileAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~ProfileAngle.md) | Gets or sets the profile angle of this surface finish symbol. |
| Property | [ProfileDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~ProfileDirection.md) | Gets or sets the profile direction of this surface finish symbol. |
| Property | [Rotated](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Rotated.md) | Obsolete. Superseded by [ISFSymbol::Orientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Orientation.md). |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetAngle.md) | Gets the angle of this surface finish symbol. |
| Method | [GetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetAnnotation.md) | Gets the annotation for this surface finish symbol. |
| Method | [GetArcAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArcAtIndex.md) | Gets information for the specified arc. |
| Method | [GetArcCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArcCount.md) | Gets the number of arcs in this surface finish symbol. |
| Method | [GetArrowHeadAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadAtIndex.md) | Gets information on the specified arrow head in this surface finish symbol. |
| Method | [GetArrowHeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadCount.md) | Gets the number of arrow heads in the surface finish symbol. |
| Method | [GetArrowHeadInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArrowHeadInfo.md) | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | [GetDirectionOfLay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetDirectionOfLay.md) | Gets the direction of lay value for this surface finish symbol. |
| Method | [GetLeaderAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderAtIndex.md) | Gets information about the specified leader on this surface finish symbol. |
| Method | [GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLeaderCount.md) | Gets the number of leaders on this surface finish symbol. |
| Method | [GetLineAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLineAtIndex.md) | Gets information for the specified line. |
| Method | [GetLineCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLineCount.md) | Gets number of line items in this surface finish symbol. |
| Method | [GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetNext.md) | Gets the next surface finish symbol in the view. |
| Method | [GetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbol.md) | Gets the type of symbol for this surface finish symbol. |
| Method | [GetSymbolAllAround](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolAllAround.md) | Gets whether this symbol is All Around or Local for this surface finish symbol. |
| Method | [GetSymbolSurfaceTexture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolSurfaceTexture.md) | Gets the symbol surface texture type for this surface finish symbol. |
| Method | [GetSymbolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbolType.md) | Obsolete. Superseded by [ISFSymbol::GetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetSymbol.md). |
| Method | [GetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetText.md) | Gets the specified text string in this surface finish symbol. |
| Method | [GetTextAngleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAngleAtIndex.md) | Gets the text angle for the specified text in this surface finish symbol. |
| Method | [GetTextAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextAtIndex.md) | Gets the specified text string from this surface finish symbol. |
| Method | [GetTextCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextCount.md) | Gets the number of text items in the surface finish symbol. |
| Method | [GetTextFontAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextFontAtIndex.md) | Gets the font used by the specified text item in this surface finish symbol. |
| Method | [GetTextHeightAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextHeightAtIndex.md) | Gets the text height for the specified piece of text in this surface finish symbol. |
| Method | [GetTextInvertAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextInvertAtIndex.md) | Gets the specified text item's invert flag. |
| Method | [GetTextPositionAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextPositionAtIndex.md) | Gets the text item's offset relative to note's text point. |
| Method | [GetTextRefPositionAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTextRefPositionAtIndex.md) | Gets the specified text item's reference position in this note, for example, upper left, lower left, center, and so on. |
| Method | [GetTriangleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTriangleAtIndex.md) | Gets the triangle at the specified index. |
| Method | [GetTriangleCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetTriangleCount.md) | Gets the number of triangles in this surface finish symbol. |
| Method | [HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~HasExtraLeader.md) | Gets whether this surface finish symbol has an extra leader line. |
| Method | [IGetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetAnnotation.md) | Gets the annotation for this surface finish symbol. |
| Method | [IGetArcAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArcAtIndex.md) | Gets information for the specified arc. |
| Method | [IGetArrowHeadAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadAtIndex.md) | Gets information on the specified arrow head in this surface finish symbol. |
| Method | [IGetArrowHeadInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArrowHeadInfo.md) | Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line. |
| Method | [IGetLeaderAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetLeaderAtIndex.md) | Gets information about the specified leader on this surface finish symbol. |
| Method | [IGetLineAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetLineAtIndex.md) | Gets information for the specified line. |
| Method | [IGetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetNext.md) | Gets the next surface finish symbol in the view. |
| Method | [IGetTextPositionAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTextPositionAtIndex.md) | Gets the text item's offset relative to note's text point. |
| Method | [IGetTriangleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetTriangleAtIndex.md) | Gets the triangle at the specified index. |
| Method | [IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IsAttached.md) | Gets whether the leader line for this surface finish symbol is attached. |
| Method | [SetAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetAngle.md) | Sets the angle for this surface finish symbol. |
| Method | [SetDirectionOfLay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetDirectionOfLay.md) | Sets the direction of lay value for this surface finish symbol. |
| Method | [SetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetSymbol.md) | Sets the type of symbol for this surface finish symbol. |
| Method | [SetSymbolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetSymbolType.md) | Obsolete. Superseded by [ISFSymbol::SetSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetSymbol.md). |
| Method | [SetText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetText.md) | Sets a text string in this surface finish symbol. |

[Top](#top)

 

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)
