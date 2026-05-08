# CreateLayer2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLayer2`

Creates a layer for this document.
Creates a layer for this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLayer2( _
   ByVal Layername As System.String, _
   ByVal LayerDesc As System.String, _
   ByVal LayerColor As System.Integer, _
   ByVal LayerStyle As System.Integer, _
   ByVal LayerWidth As System.Integer, _
   ByVal BOn As System.Boolean, _
   ByVal BPrint As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim Layername As System.String
Dim LayerDesc As System.String
Dim LayerColor As System.Integer
Dim LayerStyle As System.Integer
Dim LayerWidth As System.Integer
Dim BOn As System.Boolean
Dim BPrint As System.Boolean
Dim value As System.Boolean
 
value = instance.CreateLayer2(Layername, LayerDesc, LayerColor, LayerStyle, LayerWidth, BOn, BPrint)
```

```

System.bool CreateLayer2( 
   System.string Layername,
   System.string LayerDesc,
   System.int LayerColor,
   System.int LayerStyle,
   System.int LayerWidth,
   System.bool BOn,
   System.bool BPrint
)
```

```

System.bool CreateLayer2( 
   System.String^ Layername,
   System.String^ LayerDesc,
   System.int LayerColor,
   System.int LayerStyle,
   System.int LayerWidth,
   System.bool BOn,
   System.bool BPrint
) 
```

#### Parameters

*Layername*
:   Layer name (see **Remarks**)

*LayerDesc*
:   Description for the new layer

*LayerColor*
:   COLORREF value specifying the color of items in this layer

*LayerStyle*
:   Line style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

*LayerWidth*
:   Line width as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

*BOn*
:   True makes this layer visible, false makes it invisible

*BPrint*
:   True to print this layer when printing the document, false to not

#### Return Value

True if the layer was created successfully, false if not

Remarks

If this layer is not visible, then SOLIDWORKS does not display entities on the layer.

Do not use backslash or @ symbols in Layername.

Example

[Create Layer for Selected View (VBA)](Create_Layer_for_Selected_View_Example_VB.htm)  
[Create Layer for Selected View (VB.NET)](Create_Layer_for_Selected_View_Example_VBNET.htm)  
[Create Layer for Selected View (C#)](Create_Layer_for_Selected_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::SetCurrentLayer Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetCurrentLayer.md)  
[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)  
[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)
