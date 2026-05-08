# ReleaseStream Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReleaseStream`

Releases a previously obtained stream.
Releases a previously obtained stream.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReleaseStream( _
   ByVal StreamType As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim StreamType As System.Integer
Dim value As System.Boolean
 
value = instance.ReleaseStream(StreamType)
```

```

System.bool ReleaseStream( 
   System.int StreamType
)
```

```

System.bool ReleaseStream( 
   System.int StreamType
) 
```

#### Parameters

*StreamType*
:   1 = material stream

#### Return Value

True if stream is released, false if not

Remarks

To obtain the stream, call [IModelDocExtension::GetStream](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetStream.md).

**VB Example**

This example illustrates attaching an XML document to a stream, and then releasing the stream.

Dim swApp As Object

Sub main()

Set swApp = Application.SldWorks

Dim docext As SldWorks.ModelDocExtension

Set docext = swApp.ActiveDoc.Extension

Dim xmldoc As MSXML2.DOMDocument

Set xmldoc = CreateObject("MSXML2.DOMDocument")

Dim stat As Boolean

Dim stream

Set stream = docext.GetStream(1, stat)

xmldoc.Load (stream)

docext.ReleaseStream (1)

xmldoc.Save ("C:\temp\xmlmat.xml")

End Sub

**C++ Example**

//--------

  CComPtr<IModelDocExtension> ext;

  m\_iModelDoc2->get\_Extension(&ext);

  LPSTREAM stream = NULL;

  VARIANT\_BOOL access = 0;

  ext->IGetStream(1, &access, &stream);

  // Your code

  if (stream)

  {

  VARIANT\_BOOL status;

  ext->IReleaseStream(1, &status);

  stream->Release();

  }

  //--------

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
