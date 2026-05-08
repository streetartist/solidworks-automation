# AddLayer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~AddLayer`

Adds a layer to this drawing document.
Adds a layer to this drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddLayer( _
   ByVal NameIn As System.String, _
   ByVal DescIn As System.String, _
   ByVal ColorIn As System.Integer, _
   ByVal StyleIn As System.Integer, _
   ByVal WidthIn As System.Integer _
) As System.Integer
```

```

Dim instance As ILayerMgr
Dim NameIn As System.String
Dim DescIn As System.String
Dim ColorIn As System.Integer
Dim StyleIn As System.Integer
Dim WidthIn As System.Integer
Dim value As System.Integer
 
value = instance.AddLayer(NameIn, DescIn, ColorIn, StyleIn, WidthIn)
```

```

System.int AddLayer( 
   System.string NameIn,
   System.string DescIn,
   System.int ColorIn,
   System.int StyleIn,
   System.int WidthIn
)
```

```

System.int AddLayer( 
   System.String^ NameIn,
   System.String^ DescIn,
   System.int ColorIn,
   System.int StyleIn,
   System.int WidthIn
) 
```

#### Parameters

*NameIn*
:   Layer name

*DescIn*
:   Description for the new layer

*ColorIn*
:   COLORREF value specifying the desired color of items within this layer

*StyleIn*
:   Line style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

*WidthIn*
:   Line width as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

#### Return Value

1 if the layer was created successfully

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.md)  
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.md)
